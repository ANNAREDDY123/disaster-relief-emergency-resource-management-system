from pydantic import BaseModel, Field


class CampCreate(BaseModel):

    camp_name: str

    location: str

    district: str

    capacity: int = Field(gt=0)

    available_capacity: int = Field(gt=0)

    status: str


class CampUpdate(BaseModel):

    camp_name: str

    location: str

    district: str

    capacity: int = Field(gt=0)

    available_capacity: int = Field(gt=0)

    status: str


class CampResponse(CampCreate):

    id: int

    class Config:
        from_attributes = True
