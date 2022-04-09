def test_health(test_app):
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "health": "healthy",
        "testing": True,
    }
