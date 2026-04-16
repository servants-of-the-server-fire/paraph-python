# WebhookDelivery

Payload delivered to your webhook URL when an event occurs.  **Verifying deliveries**: Paraph follows the [Standard Webhooks](https://standardwebhooks.com) spec. Each delivery carries three headers:  - `webhook-id` — unique UUID for this delivery (use to   deduplicate retries). - `webhook-timestamp` — Unix seconds when the delivery was   sent. Reject deliveries whose timestamp is too far from   now to guard against replays. - `webhook-signature` — `v1,<base64>` where `<base64>` is the   HMAC-SHA256 of `\"{webhook-id}.{webhook-timestamp}.{body}\"`   using your webhook's secret as the key.  Language libraries that implement the spec can verify deliveries in a few lines — see `@standard-webhooks/webhooks` on npm and equivalents for other runtimes.  Failed deliveries are retried up to 5 times with exponential backoff (1s, 2s, 4s, 8s, 16s). Each attempt has a 10-second timeout. After all retries are exhausted the delivery is marked as failed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**WebhookEvent**](WebhookEvent.md) |  | 
**timestamp** | **datetime** |  | 
**data** | [**WebhookDeliveryData**](WebhookDeliveryData.md) |  | 

## Example

```python
from paraph.models.webhook_delivery import WebhookDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDelivery from a JSON string
webhook_delivery_instance = WebhookDelivery.from_json(json)
# print the JSON string representation of the object
print(WebhookDelivery.to_json())

# convert the object into a dict
webhook_delivery_dict = webhook_delivery_instance.to_dict()
# create an instance of WebhookDelivery from a dict
webhook_delivery_from_dict = WebhookDelivery.from_dict(webhook_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


