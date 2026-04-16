# paraph.WebhooksApi

All URIs are relative to *https://paraph.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Create webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{id} | Delete webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{id} | Get webhook
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /webhooks | List webhooks
[**test_webhook**](WebhooksApi.md#test_webhook) | **POST** /webhooks/{id}/test | Test webhook
[**update_webhook**](WebhooksApi.md#update_webhook) | **PATCH** /webhooks/{id} | Update webhook


# **create_webhook**
> CreateWebhook201Response create_webhook(create_webhook_request)

Create webhook

Registers a URL to receive event notifications.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.create_webhook201_response import CreateWebhook201Response
from paraph.models.create_webhook_request import CreateWebhookRequest
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
    api_instance = paraph.WebhooksApi(api_client)
    create_webhook_request = {"url":"https://example.com/webhook","events":["request.success","signer.signed"]} # CreateWebhookRequest | 

    try:
        # Create webhook
        api_response = api_instance.create_webhook(create_webhook_request)
        print("The response of WebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 

### Return type

[**CreateWebhook201Response**](CreateWebhook201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webhook created |  -  |
**400** | Invalid input |  -  |
**429** | Rate limit or quota exceeded |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(id)

Delete webhook

Permanently removes the webhook. No further deliveries will be sent.

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
    api_instance = paraph.WebhooksApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete webhook
        api_instance.delete_webhook(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Webhook deleted |  -  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> WebhookResponse get_webhook(id)

Get webhook

Returns a single webhook.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.webhook_response import WebhookResponse
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
    api_instance = paraph.WebhooksApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get webhook
        api_response = api_instance.get_webhook(id)
        print("The response of WebhooksApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook details |  -  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> WebhookListResponse list_webhooks(page=page, page_size=page_size)

List webhooks

Returns all webhooks registered in your account, newest first.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.webhook_list_response import WebhookListResponse
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
    api_instance = paraph.WebhooksApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # List webhooks
        api_response = api_instance.list_webhooks(page=page, page_size=page_size)
        print("The response of WebhooksApi->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**WebhookListResponse**](WebhookListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of webhooks for the current group |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_webhook**
> test_webhook(id)

Test webhook

Sends a test event payload to the webhook URL. Use this to verify
your endpoint is correctly receiving and processing webhook deliveries.


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
    api_instance = paraph.WebhooksApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Test webhook
        api_instance.test_webhook(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->test_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Test delivery succeeded |  -  |
**404** | Resource not found |  -  |
**502** | Upstream delivery failed |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhookResponse update_webhook(id, update_webhook_request)

Update webhook

Change the webhook URL, subscribed events, or active status. Omitted fields are left unchanged.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.update_webhook_request import UpdateWebhookRequest
from paraph.models.webhook_response import WebhookResponse
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
    api_instance = paraph.WebhooksApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_webhook_request = paraph.UpdateWebhookRequest() # UpdateWebhookRequest | 

    try:
        # Update webhook
        api_response = api_instance.update_webhook(id, update_webhook_request)
        print("The response of WebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated webhook |  -  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

