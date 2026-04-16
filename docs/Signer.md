# Signer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**signer_label** | **str** | Role label for this signer (e.g. \&quot;Employee\&quot;, \&quot;Manager\&quot;) | 
**recipient_email** | **str** |  | 
**status** | [**SignerStatus**](SignerStatus.md) |  | 
**expires_at** | **datetime** | When the signing link expires | [optional] 
**signed_at** | **datetime** | When the signer completed signing | [optional] 

## Example

```python
from paraph.models.signer import Signer

# TODO update the JSON string below
json = "{}"
# create an instance of Signer from a JSON string
signer_instance = Signer.from_json(json)
# print the JSON string representation of the object
print(Signer.to_json())

# convert the object into a dict
signer_dict = signer_instance.to_dict()
# create an instance of Signer from a dict
signer_from_dict = Signer.from_dict(signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


