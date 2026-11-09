from pathlib import Path

from cisc217_week13.main import TEMPLATES_DIR


def read_template():
    return (Path(TEMPLATES_DIR) / "index.html").read_text()


def test_template_has_character_form():
    html = read_template()

    assert 'id="character-form"' in html


def test_template_has_accessible_form_fields():
    html = read_template()

    for field in ("name", "health", "power"):
        assert f'id="{field}"' in html
        assert f'name="{field}"' in html
        assert f'for="{field}"' in html


def test_template_has_character_list():
    html = read_template()

    assert 'id="character-list"' in html


def test_template_has_refresh_button():
    html = read_template()

    assert 'id="refresh-button"' in html


def test_template_links_static_files():
    html = read_template()

    assert "styles.css" in html
    assert "app.js" in html
    assert "url_for" in html
