# object-detection-audio-feedback-assistive

MVP edge-assistive vision pipeline that detects objects, tracks them frame-to-frame, and emits audio guidance messages.

## Implemented Scope

1. Detector abstraction compatible with YOLO-style outputs.
2. Lightweight tracker abstraction inspired by Deep SORT identity continuity.
3. Audio guidance generation based on object class and approximate proximity.
4. FastAPI endpoint for frame inference simulation and integration testing.
5. Unit tests for tracking continuity and guidance generation.

## Quick Start

```bash
python -m venv .venv
# Windows PowerShell: .\\.venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8011 --reload
```

Optional security env vars:

```bash
ASSISTIVE_API_KEY=
ASSISTIVE_RATE_LIMIT_PER_MINUTE=600
```

## Endpoints

1. GET /health
2. POST /infer-frame (protected when API key is configured)

Inference requests are rate-limited per client with in-memory throttling.

## Testing

```bash
pytest -q
```

## Production Baseline

1. Architecture: `ARCHITECTURE.md`
2. Contribution guide: `CONTRIBUTING.md`
3. Security policy: `SECURITY.md`
4. Changelog: `CHANGELOG.md`
5. Collaboration context: `.claude/CLAUDE.md`
6. API docs: `docs/API.md`
7. Deployment docs: `docs/DEPLOYMENT.md`
8. Testing docs: `docs/TESTING.md`
9. CI workflow: `.github/workflows/ci.yml`
10. Release workflow: `.github/workflows/release.yml`

## Evidence

1. Pipeline tests validate tracking continuity and message prioritization behavior.
2. API tests validate auth, throttling, and contract response shape.
3. CI enforces test execution and dependency audit checks on pushes and PRs.

## Notes

This MVP uses deterministic detector inputs for portability. Replace `MockYoloV3Detector` with a real YOLOv3 or YOLOv5 inference backend on Raspberry Pi deployment.

## Limitations

1. Detector is mock-based and not connected to live camera inference hardware.
2. Rate limiting is per-instance and not shared across replicas.
3. Inference endpoint auth is shared-secret based (no role-based access model).

## Roadmap

1. Integrate real-time camera ingestion with optimized edge inference backend.
2. Add streaming endpoint support for continuous frame processing.
3. Add multilingual audio guidance templates and configurable severity tuning.
