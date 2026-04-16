# TemplateDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**metadata** | **Dict[str, str]** | Arbitrary key-value pairs (max 10 keys, key max 128 chars, value max 1024 chars) | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**fields** | [**List[ModelField]**](ModelField.md) | Form fields detected in the uploaded PDF | 
**signature_placements** | [**List[SignaturePlacement]**](SignaturePlacement.md) | Signature placement regions configured on this template | 

## Example

```python
from paraph.models.template_detail import TemplateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDetail from a JSON string
template_detail_instance = TemplateDetail.from_json(json)
# print the JSON string representation of the object
print(TemplateDetail.to_json())

# convert the object into a dict
template_detail_dict = template_detail_instance.to_dict()
# create an instance of TemplateDetail from a dict
template_detail_from_dict = TemplateDetail.from_dict(template_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


