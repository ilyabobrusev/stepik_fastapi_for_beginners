from pydantic import BaseModel, Field
from datetime import datetime


class Blog(BaseModel):
    title: str = Field(..., max_length=255)
    description: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None
    is_active: bool = Field(default=True)
    tags: list = Field(default=[])
