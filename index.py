from fastapi import FastAPI, Request
from routes.note import note

app = FastAPI()
app.include_router(note)