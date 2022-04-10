from starlette.testclient import TestClient


def test_ocr_with_file_succeeds(test_app: TestClient):
    files = {"file": open("samples/sample_urls.jpg", "rb")}
    response = test_app.post("/ocr", files=files)
    detections = response.json()["detections"]
    assert response.status_code == 200
    assert len(detections) == 3
    assert detections[0]["text"] == "Lorem ipsum"
