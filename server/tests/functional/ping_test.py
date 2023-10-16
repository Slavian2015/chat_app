from fastapi.testclient import TestClient


def test_server_ping(api_client: TestClient) -> None:
    response = api_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
