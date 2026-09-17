"""Shared helpers for the Portfolio123 example scripts.

This module centralizes the conventions every example script follows:

- Credentials are read from the ``P123_API_ID`` and ``P123_API_KEY`` environment
  variables. They are never hardcoded and never printed.
- The official ``p123api`` wrapper is used as a context manager, which is the
  documented usage pattern. These scripts are verified against **p123api 3.1.0**,
  which needs Python 3.10+. Install it as ``pip install "p123api[pandas]>=3.1.0"``:
  since p123api 3.0 pandas is an optional extra, not a dependency, and six of the
  nine scripts pass ``to_pandas=True``.
- API responses carry ``cost`` and ``quotaRemaining`` fields (the OpenAPI
  ``SharedResult`` schema). ``print_quota`` surfaces them when present.

Library module: it makes no API calls of its own and changes no account state.
"""

import os
import sys

try:
    import p123api
except ImportError:  # pragma: no cover - guidance only
    sys.exit(
        "The 'p123api' package is required (3.1.0 or newer, needs Python 3.10+).\n"
        "Install it with:\n"
        '    pip install "p123api[pandas]"\n'
        "The [pandas] extra matters: since p123api 3.0 pandas is optional and the\n"
        "wrapper imports it lazily, so to_pandas=True fails at call time without it.\n"
    )


# Environment variable names that hold the API credentials.
ENV_API_ID = "P123_API_ID"
ENV_API_KEY = "P123_API_KEY"


def get_credentials():
    """Return (api_id, api_key) as strings from the environment.

    p123api 3.1.0 accepts ``api_id`` as str or int and no longer rejects an empty
    value the way 2.x did, so this check is the only thing between a blank
    environment variable and a 401 at /auth. Strings are still what we pass.
    Fail fast with a clear message if either is missing.
    """
    api_id = os.environ.get(ENV_API_ID)
    api_key = os.environ.get(ENV_API_KEY)
    missing = [name for name, val in ((ENV_API_ID, api_id), (ENV_API_KEY, api_key)) if not val]
    if missing:
        sys.exit(
            "Missing credential environment variable(s): {}\n"
            "Set them before running, for example:\n"
            "    export {}=your_api_id\n"
            "    export {}=your_api_key\n"
            "API keys: in P123, Account Settings -> API; a paying subscription is required.".format(
                ", ".join(missing), ENV_API_ID, ENV_API_KEY
            )
        )
    # Always pass strings to the wrapper.
    return str(api_id), str(api_key)


def make_client():
    """Construct a p123api.Client from environment credentials.

    Use as a context manager so the HTTP session is closed on exit:

        with make_client() as client:
            ...
    """
    api_id, api_key = get_credentials()
    return p123api.Client(api_id=api_id, api_key=api_key)


def print_quota(result, client=None):
    """Print cost and quotaRemaining if they can be recovered.

    Three sources, tried in order:

    1. A dict response, which carries both fields directly.
    2. ``frame.attrs['raw_obj']`` -- kept under ``to_pandas=True`` by ``data``,
       ``rank_ranks`` and ``data_universe`` without asOfDt, but NOT by
       ``screen_run``, ``screen_backtest``, ``data_prices`` or ``aifactor_predict``.
    3. ``client.cost`` / ``client.quotaRemaining`` -- instance attributes added in
       p123api 3.1.0 and set after every successful request, before any DataFrame
       conversion. This is the only source for the methods in (2) that keep no raw
       object. Pass ``client`` to enable it; ``getattr`` keeps it harmless on 2.x.

    Silently does nothing when no source has a value.
    """
    obj = None
    if isinstance(result, dict):
        obj = result
    else:
        attrs = getattr(result, "attrs", None)
        if isinstance(attrs, dict):
            obj = attrs.get("raw_obj")
    if isinstance(obj, dict) and ("cost" in obj or "quotaRemaining" in obj):
        cost = obj.get("cost")
        remaining = obj.get("quotaRemaining")
    elif client is not None:
        cost = getattr(client, "cost", None)
        remaining = getattr(client, "quotaRemaining", None)
        if cost is None and remaining is None:
            return
    else:
        return
    print("API quota: cost={}, quotaRemaining={}".format(cost, remaining))


def save_csv(frame, path):
    """Save a pandas DataFrame to CSV and report the path.

    ``frame`` must be a pandas DataFrame (the scripts only call this for
    ``to_pandas=True`` results). Raises a clear error otherwise.
    """
    if not hasattr(frame, "to_csv"):
        raise TypeError("save_csv expects a pandas DataFrame (use --csv only with to_pandas output)")
    frame.to_csv(path, index=False)
    print("Saved {} rows to {}".format(len(frame), path))
