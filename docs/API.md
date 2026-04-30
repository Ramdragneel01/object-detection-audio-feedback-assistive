# API Reference

Base URL defaults to `http://127.0.0.1:8011`.

## Health and Readiness

1. `GET /health`
2. `GET /ready`
3. `GET /healthz` (alias for `/health`)
4. `GET /readyz` (alias for `/ready`)

## Authentication

`POST /infer-frame` requires `X-API-Key` only when `ASSISTIVE_API_KEY` is configured.

## Endpoints

### `GET /health`

Public health endpoint.

Response:

```json
{
  "status": "ok",
  "service": "assistive-vision"
}
```

### `POST /infer-frame`

Protected inference endpoint.

Request:

```json
{
  "frame_id": "f-1001",
  "objects": [
    {
      "label": "person",
      "confidence": 0.91,
      "bbox": [40, 30, 170, 250]
    }
  ]
}
```

Response:

```json
{
  "frame_id": "f-1001",
  "detections": [
    {
      "track_id": 1,
      "label": "person",
      "confidence": 0.91,
      "bbox": [40.0, 30.0, 170.0, 250.0],
      "distance_m": 3.25
    }
  ],
  "messages": [
    "Caution: person ahead at 3.25 meters."
  ]
}
```

Possible errors:

All API errors return a normalized payload:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "request_id": "string",
    "details": []
  }
}
```

Common error codes:

1. `unauthorized`
2. `validation_error`
3. `rate_limited`
4. `internal_error`

Common error statuses:

1. `401 Unauthorized` when API key is configured and missing or invalid (`api_key_invalid`).
2. `429 Too Many Requests` when inference request rate exceeds configured limit (`rate_limited`).
3. `429` responses include `Retry-After: 60`.
4. `422 Unprocessable Entity` for invalid payload shape (`request_validation_failed`).
