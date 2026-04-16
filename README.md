# paraph

Python client for the [Paraph API](https://paraph.dev). Upload PDF templates, fill fields, send for signing.

## Install

```bash
pip install git+https://github.com/servants-of-the-server-fire/paraph-python.git
```

## Usage

```python
from paraph import ApiClient, Configuration
from paraph.api.templates_api import TemplatesApi
from paraph.api.requests_api import RequestsApi

config = Configuration(
    host="https://paraph.dev/api/v1",
    access_token="YOUR_API_KEY",
)

with ApiClient(configuration=config) as client:
    # List templates
    templates_api = TemplatesApi(client)
    resp = templates_api.list_templates()
    for t in resp.templates:
        print(t.id, t.name)

    # Create a request (fill a PDF)
    requests_api = RequestsApi(client)
    result = requests_api.create_request({
        "template_id": "TEMPLATE_ID",
        "fields": {"name": "Jane Doe", "date": "2026-04-15"},
    })
    print(result.request.id)
```

## Auth

All requests need a Bearer token. Get an API key from your Paraph dashboard under Admin > API Keys.

```python
import os

config = Configuration(
    host="https://paraph.dev/api/v1",
    access_token=os.environ["PARAPH_API_KEY"],
)
```

## Docs

Full API reference at [paraph.dev/docs](https://paraph.dev/docs).

## License

MIT
