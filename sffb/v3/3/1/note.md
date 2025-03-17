```text
@app.get("/")
async def get_all_messages() -> dict:
    return {'Messages': messages_db}

###
{
  "Messages": [
    {
      "id": 0,
      "text": "Simple message"
    },
    {
      "id": 1,
      "text": "Simple message"
    },
    {
      "id": 2,
      "text": "Simple message"
    }
  ]
}
```

```text
@app.get("/")
async def get_all_messages() -> list[Message]:
    return messages_db

###
[
  {
    "id": 0,
    "text": "Simple message"
  },
  {
    "id": 1,
    "text": "Simple message"
  },
  {
    "id": 2,
    "text": "Simple message"
  }
]
```

```text
@app.get(path="/message/{message_id}")
async def get_message(message_id: int) -> Message:
    return messages_db[message_id] 
```