from pydantic import BaseModel


class CityCreate(BaseModel):
    name: str


class City(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True