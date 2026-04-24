# Contributing

Thanks for contributing to object-detection-audio-feedback-assistive.

## Local Setup

1. Use Python 3.11+.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Validation

Run full tests before opening a pull request:

```bash
pytest -q
```

## PR Guidelines

1. Keep changes focused and easy to review.
2. Add tests for endpoint or pipeline behavior changes.
3. Update docs when environment variables or API contracts change.
4. Do not commit credentials, access tokens, or sensitive sample data.
