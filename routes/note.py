from fastapi import APIRouter, Form, Request
from config.db import conn
from schemas.note import notesEntity
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request,):
    docs = conn.notes.notes.find({}).sort("_id", -1)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"newDocs": notesEntity(docs)}
    )


@note.post("/")
def read_note(
    title: str = Form(""),
    desc: str = Form(""),
    important: bool = Form(False),
):
    title = title.strip()
    desc = desc.strip()
    if not title or not desc:
        return RedirectResponse(url="/", status_code=303)

    conn.notes.notes.insert_one({
        "title": title,
        "desc": desc,
        "important": important,
    })
    return RedirectResponse(url="/", status_code=303)
