# RequestListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[DocumentRequestSummary]**](DocumentRequestSummary.md) |  | [optional] 
**list_info** | [**ListInfo**](ListInfo.md) |  | [optional] 

## Example

```python
from paraph.models.request_list_response import RequestListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestListResponse from a JSON string
request_list_response_instance = RequestListResponse.from_json(json)
# print the JSON string representation of the object
print(RequestListResponse.to_json())

# convert the object into a dict
request_list_response_dict = request_list_response_instance.to_dict()
# create an instance of RequestListResponse from a dict
request_list_response_from_dict = RequestListResponse.from_dict(request_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


