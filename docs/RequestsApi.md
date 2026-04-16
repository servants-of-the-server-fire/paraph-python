# paraph.RequestsApi

All URIs are relative to *https://paraph.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_request**](RequestsApi.md#cancel_request) | **POST** /requests/{id}/cancel | Cancel request
[**create_request**](RequestsApi.md#create_request) | **POST** /requests | Create request
[**download_request**](RequestsApi.md#download_request) | **GET** /requests/{id}/download | Download request PDF
[**get_request**](RequestsApi.md#get_request) | **GET** /requests/{id} | Get request detail
[**list_requests**](RequestsApi.md#list_requests) | **GET** /requests | List requests


# **cancel_request**
> RequestResponse cancel_request(id)

Cancel request

Cancels all pending signers on the request and sets the request status
to `cancelled`. Signers who have already signed are not affected.
Only requests with status `pending` can be cancelled.


### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.request_response import RequestResponse
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
    api_instance = paraph.RequestsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Request ID

    try:
        # Cancel request
        api_response = api_instance.cancel_request(id)
        print("The response of RequestsApi->cancel_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->cancel_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Request ID | 

### Return type

[**RequestResponse**](RequestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request cancelled |  -  |
**404** | Resource not found |  -  |
**409** | Invalid state transition |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request**
> RequestResponse create_request(create_request_request, idempotency_key=idempotency_key)

Create request

Fills the template's form fields and creates a request.

If `signers` is provided and the template has signature placements
configured, each signer receives a signing link via email. To provide
a signer's signature directly (skipping the email), use
`override_signature_url` in the signer object.

Omitting `signers` produces a fill-only PDF with no signing flow.

Use `GET /requests/{id}/download` to retrieve the filled or signed PDF.


### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.create_request_request import CreateRequestRequest
from paraph.models.request_response import RequestResponse
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
    api_instance = paraph.RequestsApi(api_client)
    create_request_request = {"template_id":"d290f1ee-6c54-4b01-90e6-d701748f0851","fields":{"employee_name":"Jane Doe","start_date":"2026-04-01","department":"Engineering"}} # CreateRequestRequest | 
    idempotency_key = 'idempotency_key_example' # str | Optional. If provided, ensures the request is processed at most once within 24 hours. Retries with the same key and body return the original response without creating a duplicate. Using the same key with a different request body returns 409 Conflict.  (optional)

    try:
        # Create request
        api_response = api_instance.create_request(create_request_request, idempotency_key=idempotency_key)
        print("The response of RequestsApi->create_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->create_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request_request** | [**CreateRequestRequest**](CreateRequestRequest.md)|  | 
 **idempotency_key** | **str**| Optional. If provided, ensures the request is processed at most once within 24 hours. Retries with the same key and body return the original response without creating a duplicate. Using the same key with a different request body returns 409 Conflict.  | [optional] 

### Return type

[**RequestResponse**](RequestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request created |  -  |
**400** | Invalid request or unfillable PDF |  -  |
**409** | Invalid state transition |  -  |
**429** | Rate limit or quota exceeded |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_request**
> bytes download_request(id)

Download request PDF

Returns the filled PDF. If all signers have completed, signatures are
applied to the PDF. If signing is still pending, you get the filled
PDF without signatures.


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
    api_instance = paraph.RequestsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Request ID

    try:
        # Download request PDF
        api_response = api_instance.download_request(id)
        print("The response of RequestsApi->download_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->download_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Request ID | 

### Return type

**bytes**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF file |  * Content-Disposition - attachment; filename&#x3D;\&quot;generated.pdf\&quot; or \&quot;signed.pdf\&quot; <br>  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request**
> RequestResponse get_request(id)

Get request detail

Returns the request with its field inputs and signer statuses.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.request_response import RequestResponse
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
    api_instance = paraph.RequestsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Request ID

    try:
        # Get request detail
        api_response = api_instance.get_request(id)
        print("The response of RequestsApi->get_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Request ID | 

### Return type

[**RequestResponse**](RequestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request detail including inputs and signers |  -  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_requests**
> RequestListResponse list_requests(page=page, page_size=page_size, status=status, var_from=var_from, to=to, metadata_key=metadata_key, metadata_value=metadata_value)

List requests

Returns all requests in your account, newest first.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.request_list_response import RequestListResponse
from paraph.models.request_status import RequestStatus
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
    api_instance = paraph.RequestsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    status = paraph.RequestStatus() # RequestStatus | Filter by request status (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Only return requests created on or after this timestamp (RFC 3339) (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Only return requests created on or before this timestamp (RFC 3339) (optional)
    metadata_key = 'metadata_key_example' # str | Filter by metadata key. Must be used together with metadata_value. (optional)
    metadata_value = 'metadata_value_example' # str | Filter by metadata value (exact match). Must be used together with metadata_key. (optional)

    try:
        # List requests
        api_response = api_instance.list_requests(page=page, page_size=page_size, status=status, var_from=var_from, to=to, metadata_key=metadata_key, metadata_value=metadata_value)
        print("The response of RequestsApi->list_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->list_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **status** | [**RequestStatus**](.md)| Filter by request status | [optional] 
 **var_from** | **datetime**| Only return requests created on or after this timestamp (RFC 3339) | [optional] 
 **to** | **datetime**| Only return requests created on or before this timestamp (RFC 3339) | [optional] 
 **metadata_key** | **str**| Filter by metadata key. Must be used together with metadata_value. | [optional] 
 **metadata_value** | **str**| Filter by metadata value (exact match). Must be used together with metadata_key. | [optional] 

### Return type

[**RequestListResponse**](RequestListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of requests |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

