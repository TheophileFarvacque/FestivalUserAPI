from pydantic import BaseModel


class Artist(BaseModel):
    firstname: str
    name: str
    style: str

    class Config:
        orm_mode = True
