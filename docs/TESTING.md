# Testing Guide

## Run Tests

```bash
pytest -q
```

## Coverage Areas

1. Pipeline identity tracking continuity.
2. Guidance prioritization behavior.
3. API contract behavior for inference endpoint.
4. API key enforcement on protected endpoint.
5. Rate-limit enforcement behavior.

## CI Expectations

The CI workflow validates test execution and dependency audit checks before merge.
