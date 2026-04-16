# paraph.AccountApi

All URIs are relative to *https://paraph.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountApi.md#get_account) | **GET** /account | Get account info


# **get_account**
> GetAccount200Response get_account()

Get account info

Returns the current team's plan, usage counters, and limits for the API key used in the request.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.get_account200_response import GetAccount200Response
from paraph.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paraph.dev/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = paraph.Configuration(
    host = "https://paraph.dev/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paraph.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with paraph.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paraph.AccountApi(api_client)

    try:
        # Get account info
        api_response = api_instance.get_account()
        print("The response of AccountApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAccount200Response**](GetAccount200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account info |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

