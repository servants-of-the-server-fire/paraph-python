# RequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DocumentRequest**](DocumentRequest.md) |  | [optional] 

## Example

```python
from paraph.models.request_response import RequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestResponse from a JSON string
request_response_instance = RequestResponse.from_json(json)
# print the JSON string representation of the object
print(RequestResponse.to_json())

# convert the object into a dict
request_response_dict = request_response_instance.to_dict()
# create an instance of RequestResponse from a dict
request_response_from_dict = RequestResponse.from_dict(request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


