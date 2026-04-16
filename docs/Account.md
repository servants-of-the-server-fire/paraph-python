# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_name** | **str** |  | 
**plan** | **str** |  | 
**sandbox_mode** | **bool** | Team-wide sandbox toggle. When true, every request from this team (web or API) is treated as sandbox regardless of which key is used — plan quotas are bypassed and PDFs get a SAMPLE watermark.  | 
**api_key_name** | **str** | Name of the API key used for this request | 
**api_key_sandbox** | **bool** | Whether the API key used for this request is a sandbox key. Sandbox keys are always in sandbox regardless of &#x60;sandbox_mode&#x60;. A request is effectively sandbox when either flag is true. Mode is set at key creation time and cannot be changed.  | 
**limits** | [**AccountLimits**](AccountLimits.md) |  | 
**usage** | [**AccountUsage**](AccountUsage.md) |  | 

## Example

```python
from paraph.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


