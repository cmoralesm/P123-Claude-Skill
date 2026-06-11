"""Shared helpers for the Portfolio123 example scripts.

This module centralizes the conventions every example script follows:

- Credentials are read from the ``P123_API_ID`` and ``P123_API_KEY`` environment
  variables. They are never hardcoded and never printed.
- The official ``p123api`` wrapper (``pip install p123api``, >= 2.2.0) is used as a
  context manager, which is the documented usage pattern.
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
        "The 'p123api' package is required. Install it with:\n"
        "    pip install p123api\n"
    )


# Environment variable names that hold the API credentials.
ENV_API_ID = "P123_API_ID"
ENV_API_KEY = "P123_API_KEY"


def get_credentials():
    """Return (api_id, api_key) as strings from the environment.

    The wrapper requires both values to be non-empty strings (note: the OpenAPI
    spec types ``apiId`` as an integer, but the client rejects non-strings).
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


def print_quota(result):
    """Print cost and quotaRemaining if the response carries them.

    Works on a dict response. DataFrame responses from ``to_pandas=True`` keep the
    raw object on ``frame.attrs['raw_obj']`` for some endpoints; this helper checks
    that too. Silently does nothing when the fields are absent.
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
