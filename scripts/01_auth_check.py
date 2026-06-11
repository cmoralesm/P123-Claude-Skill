"""Verify P123 API credentials and report the session token.

Purpose: confirm that P123_API_ID / P123_API_KEY authenticate successfully, then
print the configured API id and a confirmation that a Bearer token was obtained.

Endpoint(s): POST /auth (implicitly, via the wrapper's auto-authentication).
Wrapper method(s): Client.auth(), Client.get_api_id(), Client.get_token().

API quota note: /auth itself does not consume data credits and returns no
cost/quotaRemaining. The token lifetime (seconds) is sent by the server in the
X-Expires-In response header; the wrapper refreshes the token automatically on
expiry, so you rarely need to call auth() yourself (see api.md -> Authentication).

Mode: READ-ONLY. Changes no account state.

Usage:
    python 01_auth_check.py
"""

import argparse
import sys

import p123api

from p123_helpers import make_client


def main():
    parser = argparse.ArgumentParser(description="Verify P123 API credentials.")
    parser.parse_args()

    try:
        with make_client() as client:
            # Force an authentication round-trip; raises ClientException on failure.
            client.auth()
            api_id = client.get_api_id()
            token = client.get_token()
            print("Authentication succeeded.")
            print("API id: {}".format(api_id))
            print("Bearer token obtained: {}".format("yes" if token else "no"))
            print(
                "Token lifetime is reported by the server in the X-Expires-In header; "
                "the wrapper re-authenticates automatically when it expires."
            )
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
