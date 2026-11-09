"use strict";

/*
 * Week 13 Web UI Fundamentals
 *
 * Complete the TODOs below. The page should use the Week 12-style
 * FastAPI endpoints rather than storing character data in JavaScript.
 */

const characterList = document.querySelector("#character-list");
const characterForm = document.querySelector("#character-form");
const refreshButton = document.querySelector("#refresh-button");
const statusMessage = document.querySelector("#status");


function showStatus(message) {
    // TODO: Display message in the status element.
}


function renderCharacters(characters) {
    // TODO:
    // 1. Clear the existing character list.
    // 2. Create one <li> for each character.
    // 3. Display name, health, and power.
    // 4. Append each item to characterList.
}


async function loadCharacters() {
    // TODO:
    // GET /characters using fetch().
    // Convert the response to JSON.
    // Pass the result to renderCharacters().
}


async function createCharacter(event) {
    event.preventDefault();

    // TODO:
    // Read name, health, and power from the form.
    // POST JSON to /characters.
    //
    // Required request headers:
    //     "Content-Type": "application/json"
    //
    // After a successful request:
    // - clear/reset the form
    // - show a success message
    // - reload the character list
}


if (characterForm) {
    characterForm.addEventListener("submit", createCharacter);
}

if (refreshButton) {
    refreshButton.addEventListener("click", loadCharacters);
}

// TODO: Load characters when the page first opens.
