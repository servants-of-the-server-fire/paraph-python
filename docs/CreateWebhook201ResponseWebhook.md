# CreateWebhook201ResponseWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**url** | **str** |  | 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) |  | 
**active** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**secret** | **str** | HMAC secret for verifying webhook deliveries. Only returned once, when the webhook is created. Store it securely.  | [optional] 

## Example

```python
from paraph.models.create_webhook201_response_webhook import CreateWebhook201ResponseWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhook201ResponseWebhook from a JSON string
create_webhook201_response_webhook_instance = CreateWebhook201ResponseWebhook.from_json(json)
# print the JSON string representation of the object
print(CreateWebhook201ResponseWebhook.to_json())

# convert the object into a dict
create_webhook201_response_webhook_dict = create_webhook201_response_webhook_instance.to_dict()
# create an instance of CreateWebhook201ResponseWebhook from a dict
create_webhook201_response_webhook_from_dict = CreateWebhook201ResponseWebhook.from_dict(create_webhook201_response_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


