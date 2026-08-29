def NoteEntity(item) -> dict:
    return{
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"] ,
        "important": item["important"]
    }
def notesEntity(items) -> list:
    return [NoteEntity(item) for item in items]
