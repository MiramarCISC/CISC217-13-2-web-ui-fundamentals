def test_list_characters_api_still_works(client):
    response = client.get("/characters")

    assert response.status_code == 200
    assert [c["name"] for c in response.json()] == ["Aria", "Borin"]


def test_create_character_api_still_works(client):
    response = client.post(
        "/characters",
        json={"name": "Cyra", "health": 90, "power": 95},
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Cyra"
