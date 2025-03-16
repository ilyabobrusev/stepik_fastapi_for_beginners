from fastapi import FastAPI, status, Body
from pydantic import BaseModel

app = FastAPI()

messages_db = []

class Message(BaseModel):
    id: int | None = None
    text: str
    
    model_config = {
        "json_schema_extra": {
            "examples":
                [
                    {
                        "text": "Simple message",
                    }
                ]
        }
    }

@app.get("/")
async def get_all_messages() -> dict:
    return {'Messages': messages_db}


@app.get(path="/message/{message_id}")
async def get_message(message_id: int):
    return messages_db[message_id]


@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(message: Message) -> str:
    if messages_db:
        message.id = max(messages_db, key=lambda m: m.id).id + 1
    else:
        message.id = 0
    messages_db.append(message)
    return "Message created!"


@app.put("/message/{message_id}")
async def update_message(message_id: int, message: str = Body()) -> str:
    edit_message = messages_db[message_id]
    edit_message.text = message
    return "Message updated!"


@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    messages_db.pop(message_id)
    return f"Message ID={message_id} deleted!"


@app.delete("/")
async def kill_message_all() -> str:
    messages_db.clear()
    return "All messages deleted!"
