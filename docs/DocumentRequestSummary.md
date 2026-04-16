# DocumentRequestSummary

Compact request representation returned in list endpoints. Use GET /requests/{id} for full details including inputs, metadata, and signers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**template_id** | **UUID** |  | 
**title** | **str** |  | [optional] 
**status** | [**RequestStatus**](RequestStatus.md) |  | 
**has_signing** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from paraph.models.document_request_summary import DocumentRequestSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRequestSummary from a JSON string
document_request_summary_instance = DocumentRequestSummary.from_json(json)
# print the JSON string representation of the object
print(DocumentRequestSummary.to_json())

# convert the object into a dict
document_request_summary_dict = document_request_summary_instance.to_dict()
# create an instance of DocumentRequestSummary from a dict
document_request_summary_from_dict = DocumentRequestSummary.from_dict(document_request_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


