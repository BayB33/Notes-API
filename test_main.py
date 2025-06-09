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

#def test_get_notes():
#    assert response.status_code == 200