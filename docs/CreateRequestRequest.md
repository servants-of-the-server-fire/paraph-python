# CreateRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | ID of the template to fill | 
**fields** | **Dict[str, str]** | Map of field names to values. Text fields accept strings. Checkbox fields accept \&quot;checked\&quot; or \&quot;unchecked\&quot;. | [optional] 
**signers** | [**Dict[str, SignerInput]**](SignerInput.md) | Map of signer label to signer configuration. Each key is a signer label defined in the template&#39;s signature placements. Omit entirely for fill-only requests.  | [optional] 
**title** | **str** | Display title for the request. Defaults to the template name. Shown in emails and dashboards. | [optional] 
**message** | **str** | Custom message included in signing emails sent to signers. | [optional] 
**metadata** | **Dict[str, str]** | Arbitrary key-value pairs for your own use (max 10 keys, key max 128 chars, value max 1024 chars) | [optional] 
**allow_typed_signature** | **bool** | Whether signers can type their name as a signature instead of drawing or uploading one. Defaults to true.  | [optional] [default to True]

## Example

```python
from paraph.models.create_request_request import CreateRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestRequest from a JSON string
create_request_request_instance = CreateRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRequestRequest.to_json())

# convert the object into a dict
create_request_request_dict = create_request_request_instance.to_dict()
# create an instance of CreateRequestRequest from a dict
create_request_request_from_dict = CreateRequestRequest.from_dict(create_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


