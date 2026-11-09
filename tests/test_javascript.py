import re


def test_javascript_uses_fetch(client):
    javascript = client.get("/static/app.js").text

    assert re.search(r"await\s+fetch\s*\(", javascript)


def test_javascript_loads_characters_endpoint(client):
    javascript = client.get("/static/app.js").text

    assert re.search(
        r"await\s+fetch\s*\(\s*[\"']/characters[\"']",
        javascript,
    )


def test_javascript_posts_json(client):
    javascript = client.get("/static/app.js").text

    assert re.search(r"method\s*:\s*[\"']POST[\"']", javascript)
    assert "JSON.stringify" in javascript


def test_javascript_updates_dom(client):
    javascript = client.get("/static/app.js").text

    assert "document.createElement" in javascript
    assert ".appendChild(" in javascript
