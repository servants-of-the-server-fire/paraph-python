# WebhookDelivery

Payload delivered to your webhook URL when an event occurs.  Deliveries include an `X-Signature-256` header containing `sha256=<hex>` where `<hex>` is the HMAC-SHA256 of the request body using the webhook's secret as the key. Verify this to confirm the delivery came from Paraph.  Failed deliveries are retried up to 5 times with exponential backoff (1s, 2s, 4s, 8s, 16s). Each attempt has a 10-second timeout. After all retries are exhausted the delivery is marked as failed. 

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


