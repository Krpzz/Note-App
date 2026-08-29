import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


mongo_client = MongoClient(
    os.getenv("MONGODB_URI", "mongodb://localhost:27017/"),
    serverSelectionTimeoutMS=2000,
)
mongo_database = os.getenv("MONGODB_DATABASE", "notes")
mongo_collection = os.getenv("MONGODB_COLLECTION", "notes")


def get_mongodb_data():
    documents = list(mongo_client[mongo_database][mongo_collection].find({}).limit(20))

    for document in documents:
        document["_id"] = str(document["_id"])

    return documents


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    mongodb_data = []
    mongodb_error = None

    try:
        mongodb_data = get_mongodb_data()
    except PyMongoError as exc:
        mongodb_error = str(exc)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "mongodb_data": mongodb_data,
            "mongodb_error": mongodb_error,
            "mongo_database": mongo_database,
            "mongo_collection": mongo_collection,
        },
    )


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )
