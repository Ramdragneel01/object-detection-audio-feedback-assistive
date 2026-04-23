# object-detection-audio-feedback-assistive

MVP edge-assistive vision pipeline that detects objects, tracks them frame-to-frame, and emits audio guidance messages.

## Implemented Scope

1. Detector abstraction compatible with YOLO-style outputs.
2. Lightweight tracker abstraction inspired by Deep SORT identity continuity.
3. Audio guidance generation based on object class and approximate proximity.
4. FastAPI endpoint for frame inference simulation and integration testing.
5. Unit tests for tracking continuity and guidance generation.

## Run

```bash
python -m venv .venv
# Windows PowerShell: .\\.venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8011 --reload
```

## Endpoints

1. GET /health
2. POST /infer-frame

## Notes

This MVP uses deterministic detector inputs for portability. Replace `MockYoloV3Detector` with a real YOLOv3 or YOLOv5 inference backend on Raspberry Pi deployment.
