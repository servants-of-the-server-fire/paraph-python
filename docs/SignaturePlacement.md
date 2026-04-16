# SignaturePlacement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**signer_label** | **str** | Label identifying which signer this placement belongs to | 
**page_number** | **int** |  | 
**x** | **float** | X coordinate in PDF points from the left edge of the page | 
**y** | **float** | Y coordinate in PDF points from the bottom edge of the page | 
**width** | **float** |  | 
**height** | **float** |  | 

## Example

```python
from paraph.models.signature_placement import SignaturePlacement

# TODO update the JSON string below
json = "{}"
# create an instance of SignaturePlacement from a JSON string
signature_placement_instance = SignaturePlacement.from_json(json)
# print the JSON string representation of the object
print(SignaturePlacement.to_json())

# convert the object into a dict
signature_placement_dict = signature_placement_instance.to_dict()
# create an instance of SignaturePlacement from a dict
signature_placement_from_dict = SignaturePlacement.from_dict(signature_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


