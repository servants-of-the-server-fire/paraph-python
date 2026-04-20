# paraph.AuthApi

All URIs are relative to *https://paraph.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register**](AuthApi.md#register) | **POST** /auth/register | Register a new account


# **register**
> Register201Response register(register_request)

Register a new account

Creates a new user account and sends a verification email. The user must
click the link in the email before they can log in. After verification,
retrieve your API key from the web dashboard at https://paraph.dev.

Rate limited to 5 registrations per hour per IP address.


### Example


```python
import paraph
from paraph.models.register201_response import Register201Response
from paraph.models.register_request import RegisterRequest
from paraph.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paraph.dev/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = paraph.Configuration(
    host = "https://paraph.dev/api/v1"
)


# Enter a context with an instance of the API client
with paraph.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paraph.AuthApi(api_client)
    register_request = {"email":"dev@example.com","password":"s3curePa55word"} # RegisterRequest | 

    try:
        # Register a new account
        api_response = api_instance.register(register_request)
        print("The response of AuthApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**Register201Response**](Register201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Account created — check email to verify |  * X-Request-Id -  <br>  |
**400** | Invalid input |  -  |
**403** | Action not permitted |  -  |
**409** | Email already registered |  * X-Request-Id -  <br>  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

