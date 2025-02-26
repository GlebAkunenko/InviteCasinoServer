from pydantic import BaseModel

class Card(BaseModel):
    value: int
    style: str

class Result(BaseModel):
    slots: list[Card]
    win: int