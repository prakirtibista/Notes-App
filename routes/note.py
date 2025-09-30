from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config.db import db
from schemas.note import noteEntity, notesEntity
from models.note import Note

note = APIRouter()

# Templates and static files
templates = Jinja2Templates(directory="templates")
note.mount("/static", StaticFiles(directory="static"), name="static")


@note.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    docs = db.notes.find()
    newDocs = [noteEntity(doc) for doc in docs]
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/", response_class=HTMLResponse)
async def add_note(
    request: Request,
    title: str = Form(...),
    desc: str = Form(...),
    important: str | None = Form(None)
):
    doc = {
        "title": title,
        "desc": desc,
        "important": True if important == "on" else False
    }
    db.notes.insert_one(doc)
    # After inserting, redirect back to the home page
    return RedirectResponse(url="/", status_code=303)
