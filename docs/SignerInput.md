# SignerInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**override_signature_url** | **str** | URL to a PNG signature image. When provided, the image is downloaded and stored, the signer is immediately marked as signed, and no signing email is sent.  | [optional] 

## Example

```python
from paraph.models.signer_input import SignerInput

# TODO update the JSON string below
json = "{}"
# create an instance of SignerInput from a JSON string
signer_input_instance = SignerInput.from_json(json)
# print the JSON string representation of the object
print(SignerInput.to_json())

# convert the object into a dict
signer_input_dict = signer_input_instance.to_dict()
# create an instance of SignerInput from a dict
signer_input_from_dict = SignerInput.from_dict(signer_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


