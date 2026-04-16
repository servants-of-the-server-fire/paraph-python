# WebhookEvent

Event types. `request.created`, `request.success`, `request.cancelled`, and `request.error` are dispatched for request lifecycle transitions. `signer.viewed` fires each time a signer loads their signing link, `signer.signed` fires when a signer completes signing, and `signer.declined` fires when a signer explicitly declines to sign. `webhook.test` is sent when you use the test endpoint to verify your webhook URL. 

## Enum

* `REQUEST_DOT_CREATED` (value: `'request.created'`)

* `REQUEST_DOT_SUCCESS` (value: `'request.success'`)

* `REQUEST_DOT_CANCELLED` (value: `'request.cancelled'`)

* `REQUEST_DOT_ERROR` (value: `'request.error'`)

* `SIGNER_DOT_VIEWED` (value: `'signer.viewed'`)

* `SIGNER_DOT_SIGNED` (value: `'signer.signed'`)

* `SIGNER_DOT_DECLINED` (value: `'signer.declined'`)

* `WEBHOOK_DOT_TEST` (value: `'webhook.test'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


