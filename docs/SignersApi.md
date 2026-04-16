# paraph.SignersApi

All URIs are relative to *https://paraph.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_signer_signature**](SignersApi.md#download_signer_signature) | **GET** /requests/{id}/signers/{sid}/signature | Download signer signature
[**resend_signing_link**](SignersApi.md#resend_signing_link) | **POST** /requests/{id}/signers/{sid}/resend | Resend signing link


# **download_signer_signature**
> bytes download_signer_signature(id, sid)

Download signer signature

Returns the stored signature image (PNG) for a signer who has completed
signing, either via the signing page or a pre-provided override_signature_url.


### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
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
    api_instance = paraph.SignersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Request ID
    sid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Signer ID

    try:
        # Download signer signature
        api_response = api_instance.download_signer_signature(id, sid)
        print("The response of SignersApi->download_signer_signature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignersApi->download_signer_signature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Request ID | 
 **sid** | **UUID**| Signer ID | 

### Return type

**bytes**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signature image |  -  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_signing_link**
> ResendSigningLink200Response resend_signing_link(id, sid)

Resend signing link

Generates a new signing link and resends the signing email.
The previous link is invalidated. Only works for signers
with status `pending`.


### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.resend_signing_link200_response import ResendSigningLink200Response
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
    api_instance = paraph.SignersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Request ID
    sid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Signer ID

    try:
        # Resend signing link
        api_response = api_instance.resend_signing_link(id, sid)
        print("The response of SignersApi->resend_signing_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignersApi->resend_signing_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Request ID | 
 **sid** | **UUID**| Signer ID | 

### Return type

[**ResendSigningLink200Response**](ResendSigningLink200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New signing link sent |  -  |
**409** | Invalid state transition |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

