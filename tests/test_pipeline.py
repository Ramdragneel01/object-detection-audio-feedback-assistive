from src.pipeline import AssistiveVisionPipeline, build_guidance_messages


def test_pipeline_maintains_track_id_for_nearby_frame_motion():
    pipeline = AssistiveVisionPipeline()

    frame_one = pipeline.process_frame(
        [
            {
                "label": "person",
                "confidence": 0.91,
                "bbox": [40, 30, 170, 250],
            }
        ]
    )

    frame_two = pipeline.process_frame(
        [
            {
                "label": "person",
                "confidence": 0.89,
                "bbox": [48, 34, 178, 255],
            }
        ]
    )

    assert frame_one["detections"][0]["track_id"] == frame_two["detections"][0]["track_id"]


def test_guidance_messages_prioritize_nearest_objects():
    detections = [
        type("Obj", (), {"label": "car", "distance_m": 3.2})(),
        type("Obj", (), {"label": "pole", "distance_m": 1.1})(),
        type("Obj", (), {"label": "bicycle", "distance_m": 2.4})(),
    ]

    messages = build_guidance_messages(detections)

    assert messages
    assert messages[0].startswith("Warning")
    assert "pole" in messages[0]
