import re


def test_css_is_served(client):
    response = client.get("/static/styles.css")

    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]


def test_javascript_is_served(client):
    response = client.get("/static/app.js")

    assert response.status_code == 200
    assert "javascript" in response.headers["content-type"]


def test_css_demonstrates_box_model(client):
    css = client.get("/static/styles.css").text

    assert re.search(r"padding\s*:", css)
    assert re.search(r"border(?:-[a-z]+)?\s*:", css)
    assert re.search(r"margin(?:-[a-z]+)?\s*:", css)
