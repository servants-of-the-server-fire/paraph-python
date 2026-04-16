# DocumentRequest

Full request representation returned by detail and create endpoints. Includes inputs, metadata, and signers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**template_id** | **UUID** |  | 
**title** | **str** | Display title for the request | [optional] 
**message** | **str** | Custom message included in signing emails | [optional] 
**status** | [**RequestStatus**](RequestStatus.md) |  | 
**has_signing** | **bool** | Whether this request includes signers | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**inputs** | **Dict[str, str]** | Field values used to fill the template | [optional] 
**metadata** | **Dict[str, str]** | Arbitrary key-value pairs for your own use (max 10 keys, key max 128 chars, value max 1024 chars) | [optional] 
**signers** | [**List[Signer]**](Signer.md) | Signers attached to this request, if any | [optional] 

## Example

```python
from paraph.models.document_request import DocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRequest from a JSON string
document_request_instance = DocumentRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentRequest.to_json())

# convert the object into a dict
document_request_dict = document_request_instance.to_dict()
# create an instance of DocumentRequest from a dict
document_request_from_dict = DocumentRequest.from_dict(document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


