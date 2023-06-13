import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Item(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    type_id: int = Field(...)
    reprocess: object = Field(...)
    buy_orders: list = Field(...)
    sell_orders: list = Field(...)

    
