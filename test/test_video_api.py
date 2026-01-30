import time
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_video_ingestion_and_processing():
    response = client.post(
        "/api/v1/videos",
        data={"video_url": "https://example.com/video.mp4"}
    )
    assert response.status_code == 200

    data = response.json()
    video_id = data["video_id"]
    assert data["status"] == "UPLOADED"

    # Poll status
    time.sleep(6)
    status_resp = client.get(f"/api/v1/videos/{video_id}")
    assert status_resp.status_code == 200
    assert status_resp.json()["status"] == "COMPLETED"
