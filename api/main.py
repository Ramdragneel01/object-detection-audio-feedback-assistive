from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.pipeline import AssistiveVisionPipeline


class FrameRequest(BaseModel):
    frame_id: str = Field(min_length=1, max_length=120)
    objects: list[dict[str, Any]] = Field(default_factory=list, max_length=200)


app = FastAPI(title="object-detection-audio-feedback-assistive", version="0.1.0")
pipeline = AssistiveVisionPipeline()


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "assistive-vision",
    }


@app.post("/infer-frame")
def infer_frame(payload: FrameRequest) -> dict[str, Any]:
    result = pipeline.process_frame(payload.objects)
    return {
        "frame_id": payload.frame_id,
        **result,
    }
