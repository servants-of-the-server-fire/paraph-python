# ListInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**num_pages** | **int** |  | 
**num_results** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from paraph.models.list_info import ListInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ListInfo from a JSON string
list_info_instance = ListInfo.from_json(json)
# print the JSON string representation of the object
print(ListInfo.to_json())

# convert the object into a dict
list_info_dict = list_info_instance.to_dict()
# create an instance of ListInfo from a dict
list_info_from_dict = ListInfo.from_dict(list_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


