# AccountUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **int** | Requests created in the last 30 days | 
**signing_requests** | **int** | Signing tasks created in the last 30 days | 
**templates** | **int** | Total templates in the account | 
**members** | **int** | Total team members | 

## Example

```python
from paraph.models.account_usage import AccountUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUsage from a JSON string
account_usage_instance = AccountUsage.from_json(json)
# print the JSON string representation of the object
print(AccountUsage.to_json())

# convert the object into a dict
account_usage_dict = account_usage_instance.to_dict()
# create an instance of AccountUsage from a dict
account_usage_from_dict = AccountUsage.from_dict(account_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


