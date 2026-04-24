# Deployment Guide

## Prerequisites

1. Python 3.11+
2. pip

## Install and Run

```bash
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8011
```

## Environment Variables

1. `ASSISTIVE_API_KEY` (optional; enables API key auth on `/infer-frame`)
2. `ASSISTIVE_RATE_LIMIT_PER_MINUTE` (default `600`)

## Runtime Security Notes

1. Store API keys in a secret manager.
2. Use HTTPS and ingress controls in production.
3. Keep request payload size bounded at reverse proxy and app gateway layers.

## CI and Release

1. CI workflow: `.github/workflows/ci.yml`
2. Release workflow: `.github/workflows/release.yml`
