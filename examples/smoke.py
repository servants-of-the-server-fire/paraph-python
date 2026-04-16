"""Smoke test for the Paraph Python SDK.

Calls GET /account and GET /templates against a live instance,
prints the results. Read-only; safe to run.

Usage:
    PARAPH_API_KEY=your-key python examples/smoke.py

Optional:
    PARAPH_BASE_URL=http://localhost:8080/api/v1 python examples/smoke.py
"""
import os
import sys

from paraph import ApiClient, Configuration
from paraph.api.account_api import AccountApi
from paraph.api.templates_api import TemplatesApi


def main() -> None:
    api_key = os.environ.get("PARAPH_API_KEY")
    if not api_key:
        print("PARAPH_API_KEY must be set", file=sys.stderr)
        sys.exit(1)

    host = os.environ.get("PARAPH_BASE_URL", "https://paraph.dev/api/v1")
    config = Configuration(host=host, access_token=api_key)

    with ApiClient(configuration=config) as client:
        print("→ GET /account")
        resp = AccountApi(client).get_account()
        a = resp.account
        print(f"  team={a.team_name!r} plan={a.plan} sandbox={a.sandbox_mode}")

        print("→ GET /templates")
        tmpls = TemplatesApi(client).list_templates()
        print(f"  {len(tmpls.templates)} template(s)")
        for i, t in enumerate(tmpls.templates[:5]):
            print(f"  - {t.id}  {t.name!r}")
        if len(tmpls.templates) > 5:
            print(f"  ... ({len(tmpls.templates) - 5} more)")

        print("ok")


if __name__ == "__main__":
    main()
