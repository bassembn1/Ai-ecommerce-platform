from pydantic import BaseModel

class EventCreate(BaseModel):
    event_type: str
    product_id: int | None = None
    event_data: dict | None = None