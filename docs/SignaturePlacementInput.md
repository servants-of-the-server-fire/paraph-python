# SignaturePlacementInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_label** | **str** |  | 
**page_number** | **int** |  | 
**x** | **float** |  | 
**y** | **float** |  | 
**width** | **float** |  | 
**height** | **float** |  | 

## Example

```python
from paraph.models.signature_placement_input import SignaturePlacementInput

# TODO update the JSON string below
json = "{}"
# create an instance of SignaturePlacementInput from a JSON string
signature_placement_input_instance = SignaturePlacementInput.from_json(json)
# print the JSON string representation of the object
print(SignaturePlacementInput.to_json())

# convert the object into a dict
signature_placement_input_dict = signature_placement_input_instance.to_dict()
# create an instance of SignaturePlacementInput from a dict
signature_placement_input_from_dict = SignaturePlacementInput.from_dict(signature_placement_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


