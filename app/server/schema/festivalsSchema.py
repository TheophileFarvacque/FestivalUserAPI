from pydantic import BaseModel


class Festival(BaseModel):
    name: str
    city: str
    zipcode: int
    address: str

    class Config:
        orm_mode = True
