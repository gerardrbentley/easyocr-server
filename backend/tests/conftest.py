import pytest
from fastapi.testclient import TestClient

from app.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=1)


@pytest.fixture(scope="module")
def test_app():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        # testing
        yield test_client

    # tear down
