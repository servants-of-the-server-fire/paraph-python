# AccountLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests_per_month** | **int** | -1 means unlimited | 
**signing_requests_per_month** | **int** | -1 means unlimited | 
**max_templates** | **int** | -1 means unlimited | 
**max_members** | **int** | -1 means unlimited | 

## Example

```python
from paraph.models.account_limits import AccountLimits

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLimits from a JSON string
account_limits_instance = AccountLimits.from_json(json)
# print the JSON string representation of the object
print(AccountLimits.to_json())

# convert the object into a dict
account_limits_dict = account_limits_instance.to_dict()
# create an instance of AccountLimits from a dict
account_limits_from_dict = AccountLimits.from_dict(account_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


