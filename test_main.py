from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue dans ton API de notes 🎉"}

def test_create_note():
    note_data = {
        "id": 1,
        "title": "Test",
        "content": "Ceci est un test"
    }
    response = client.post("/notes", json=note_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Note ajoutee avec succes"}

def test_get_notes():
    note_data = {
        "id": 42,
        "title": "Test",
        "content": "This is just a test"
    }
    post_response = client.post("/notes", json=note_data)
    assert post_response.status_code == 200

    get_response = client.get("/notes")
    assert get_response.status_code == 200

    notes = get_response.json()
    assert isinstance(notes, list)
    assert any(note["id"] == 42 and note["title"] == "Test" for note in notes)

def test_delete_note():
    note_data = {
        "id": 44,
        "title": "Test",
        "content": "This is just a test"
    }
    post_response = client.post("/notes", json=note_data)
    assert post_response.status_code == 200

    delete_response = client.delete(f"/notes/{note_data['id']}")
    assert delete_response.status_code == 200

    get_response = client.get("/notes")
    notes = get_response.json()
    assert all(note["id"] != note_data["id"] for note in notes)

#Cree une note initiale
def test_update_note():
    original_note = {
        "id": 50,
        "title": "Test Original",
        "content": "This is the original"
    }
    post_response = client.post("/notes", json=original_note)
    assert post_response.status_code == 200

    #Definir le contenu de la nouvelle note
    updated_data = {
        "title": "New Title"
        "content": "Updated Content"
    }