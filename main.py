from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException

app = FastAPI()
#Cree une classe qui determine le fonctionnement de l'objet Note
class Note(BaseModel):
    id: int
    title: str
    content: str

#Cree une variable notes qui va contenir la liste des notes
notes: List[Note] = []

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans ton API de notes 🎉"}

#Creation d'une note
@app.post("/notes")
def create_note(note: Note):
    #verifie si une note avec cet ID existe deja
    for existing_note in notes:
        if existing_note.id == note.id:
            raise HTTPException(status_code=400, detail="Une note avec cet ID existe deja.")
    notes.append(note)
    return {"message": "Note ajoutee avec succes"}

#Recupere toutes les notes
@app.get("/notes")
def get_notes():
    return notes

#Supprime une note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for index, note in enumerate(notes):
        if note.id == note_id:
            del notes[index]
            return {"message": "Note supprimee avec succes"}
    raise HTTPException(status_code=404, detail="Note non trouvee")

#Modifier une note
@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes[index] = updated_note
            return {"message": "Note modifiee avec succes"}
    raise HTTPException(status_code=404, detail="Note non trouvee")

#test auto push 4