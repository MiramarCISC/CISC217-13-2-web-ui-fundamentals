def test_home_returns_html(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_home_contains_page_title(client):
    response = client.get("/")

    assert "Character Manager" in response.text
