# Security Policy

## Supported Versions

The latest default-branch release is supported for security updates.

## Reporting a Vulnerability

Please report security issues privately using GitHub Security Advisories or direct maintainer contact.

Include:

1. Clear issue description.
2. Reproduction steps.
3. Affected endpoint/module.
4. Potential impact and suggested mitigation.

## Secure Usage Guidance

1. Set `ASSISTIVE_API_KEY` in environments exposed to untrusted clients.
2. Tune `ASSISTIVE_RATE_LIMIT_PER_MINUTE` to expected traffic profiles.
3. Avoid storing raw personal or sensitive camera metadata in logs.
4. Use HTTPS and network controls for deployment endpoints.
