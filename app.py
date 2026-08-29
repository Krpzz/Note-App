from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient # type: ignore


app = FastAPI()
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://kripeshkhadka66_db_user:sqf7J47nQ7wNnEg7@notes.43zz0yx.mongodb.net")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )
