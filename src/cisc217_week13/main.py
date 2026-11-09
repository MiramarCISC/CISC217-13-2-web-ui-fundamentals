"""FastAPI application for the Week 13 Web UI Fundamentals lab."""

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="CISC 217 Character Manager")

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)

templates = Jinja2Templates(directory=TEMPLATES_DIR)


class CharacterCreate(BaseModel):
    """Request model for creating a character."""

    name: str
    health: int
    power: int


characters: dict[int, dict] = {
    1: {"id": 1, "name": "Aria", "health": 100, "power": 85},
    2: {"id": 2, "name": "Borin", "health": 120, "power": 70},
}


@app.get("/")
def home(request: Request):
    """Render the browser user interface."""
    # TODO: Render index.html using TemplateResponse.
    # Pass a page title through the template context.
    raise NotImplementedError


@app.get("/characters")
def list_characters(minimum_power: int = 0, limit: int = 10):
    """Return characters filtered by minimum power and limited in count."""
    filtered = [
        character
        for character in characters.values()
        if character["power"] >= minimum_power
    ]
    return filtered[:limit]


@app.get("/characters/{character_id}")
def get_character(character_id: int):
    """Return one character or raise 404 if it does not exist."""
    character = characters.get(character_id)

    if character is None:
        raise HTTPException(
            status_code=404,
            detail="Character not found",
        )

    return character


@app.post("/characters", status_code=201)
def create_character(character: CharacterCreate):
    """Create and return a new character."""
    character_id = max(characters, default=0) + 1

    new_character = {
        "id": character_id,
        **character.model_dump(),
    }

    characters[character_id] = new_character
    return new_character


@app.delete("/characters/{character_id}")
def delete_character(character_id: int):
    """Delete a character or raise 404."""
    if character_id not in characters:
        raise HTTPException(
            status_code=404,
            detail="Character not found",
        )

    del characters[character_id]
    return {"deleted": True}
