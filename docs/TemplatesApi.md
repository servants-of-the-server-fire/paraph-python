# paraph.TemplatesApi

All URIs are relative to *https://paraph.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplatesApi.md#create_template) | **POST** /templates | Create template
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /templates/{id} | Delete template
[**download_template**](TemplatesApi.md#download_template) | **GET** /templates/{id}/download | Download template PDF
[**get_template**](TemplatesApi.md#get_template) | **GET** /templates/{id} | Get template detail
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /templates | List templates
[**update_template**](TemplatesApi.md#update_template) | **PATCH** /templates/{id} | Update template


# **create_template**
> TemplateResponse create_template(name, file=file, file_url=file_url)

Create template

Upload a PDF with named form fields. Paraph detects the fields automatically.

**Provide exactly one of `file` or `file_url`.** Requests with neither or both return `400 Bad Request`. This constraint is validated server-side — OpenAPI doesn't support expressing `oneOf` inside a multipart request body, so it's documented in prose.


### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.template_response import TemplateResponse
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
    api_instance = paraph.TemplatesApi(api_client)
    name = 'name_example' # str | Display name for the template
    file = None # bytes | PDF file with AcroForm fields (mutually exclusive with `file_url`) (optional)
    file_url = 'file_url_example' # str | URL to fetch the PDF from (mutually exclusive with `file`) (optional)

    try:
        # Create template
        api_response = api_instance.create_template(name, file=file, file_url=file_url)
        print("The response of TemplatesApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Display name for the template | 
 **file** | **bytes**| PDF file with AcroForm fields (mutually exclusive with &#x60;file_url&#x60;) | [optional] 
 **file_url** | **str**| URL to fetch the PDF from (mutually exclusive with &#x60;file&#x60;) | [optional] 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template created |  -  |
**400** | Validation error or PDF could not be parsed |  -  |
**429** | Rate limit or quota exceeded |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(id)

Delete template

Permanently removes the template. Existing requests created from it are not affected.

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
    api_instance = paraph.TemplatesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete template
        api_instance.delete_template(id)
    except Exception as e:
        print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
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
**204** | Template deleted |  -  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_template**
> bytes download_template(id)

Download template PDF

Returns the original PDF that was uploaded when the template was created.

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
    api_instance = paraph.TemplatesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Download template PDF
        api_response = api_instance.download_template(id)
        print("The response of TemplatesApi->download_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->download_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

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

# **get_template**
> TemplateResponse get_template(id)

Get template detail

Returns the template with its detected form fields and signature placements.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.template_response import TemplateResponse
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
    api_instance = paraph.TemplatesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get template detail
        api_response = api_instance.get_template(id)
        print("The response of TemplatesApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template detail with fields |  -  |
**404** | Resource not found |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> TemplateListResponse list_templates(page=page, page_size=page_size)

List templates

Returns all templates in your account, newest first.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.template_list_response import TemplateListResponse
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
    api_instance = paraph.TemplatesApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # List templates
        api_response = api_instance.list_templates(page=page, page_size=page_size)
        print("The response of TemplatesApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**TemplateListResponse**](TemplateListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of templates |  -  |
**400** | Invalid input |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> TemplateResponse update_template(id, update_template_request)

Update template

Change the template name, metadata, or signature placements. Omitted fields are left unchanged.

### Example

* Bearer Authentication (bearerAuth):

```python
import paraph
from paraph.models.template_response import TemplateResponse
from paraph.models.update_template_request import UpdateTemplateRequest
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
    api_instance = paraph.TemplatesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_template_request = {"name":"Employment Agreement v2","metadata":{"category":"hr","year":"2026"},"signature_placements":[{"signer_label":"Employee","page_number":1,"x":100.0,"y":650.0,"width":200.0,"height":50.0}]} # UpdateTemplateRequest | 

    try:
        # Update template
        api_response = api_instance.update_template(id, update_template_request)
        print("The response of TemplatesApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **update_template_request** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)|  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated template |  -  |
**400** | Validation error |  -  |
**404** | Resource not found |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit or quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

