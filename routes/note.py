from fastapi import APIRouter, Request
from models.note import Note
from config.db import conn
from schemas.note import notesEntity, NoteEntity
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

note = APIRouter()


note.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request,):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({ # type: ignore
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse(
        request=request, name="index.html", context={"newDocs": ["newDocs"]}
    )

@note.post("/")
def read_note(note : Note):
    inserted_note = conn.notes.notes.insert_one(dict(note))
    return NoteEntity(conn.notes.notes.find_one({"_id": inserted_note.inserted_id}))