# API Reference

Base URL defaults to `http://127.0.0.1:8011`.

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

1. `401 Unauthorized` when API key is configured and missing or invalid.
2. `429 Too Many Requests` when inference request rate exceeds configured limit.
3. `422 Unprocessable Entity` for invalid payload shape.
