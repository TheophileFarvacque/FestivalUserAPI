from pydantic import BaseModel


class ArtistBase(BaseModel):
    firstname: str
    name: str
    style: str

    class Config:
        orm_mode = True
