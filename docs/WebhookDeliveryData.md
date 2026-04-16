# WebhookDeliveryData

Event-specific payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **UUID** |  | [optional] 
**template_id** | **UUID** |  | [optional] 
**signer_id** | **UUID** | Present for signer.* events | [optional] 
**signer_label** | **str** | Present for signer.* events | [optional] 
**recipient_email** | **str** | Present for signer.* events | [optional] 

## Example

```python
from paraph.models.webhook_delivery_data import WebhookDeliveryData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryData from a JSON string
webhook_delivery_data_instance = WebhookDeliveryData.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryData.to_json())

# convert the object into a dict
webhook_delivery_data_dict = webhook_delivery_data_instance.to_dict()
# create an instance of WebhookDeliveryData from a dict
webhook_delivery_data_from_dict = WebhookDeliveryData.from_dict(webhook_delivery_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


