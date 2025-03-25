def test_login(client):
    response = client.post("/auth/login", data={"username": "admin@test.com", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()