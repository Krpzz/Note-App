def NoteEntity(item) -> dict:
    return{
        "_id": str(item["_id"]),
        "title": item.get("title") or item.get("note") or item.get("whats_new") or "",
        "desc": item.get("desc") or item.get("more") or "",
        "important": item.get("important", False)
    }
def notesEntity(items) -> list:
    return [NoteEntity(item) for item in items]
