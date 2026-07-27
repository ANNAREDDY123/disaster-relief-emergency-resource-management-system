from pydantic import BaseModel, Field


class VictimCreate(BaseModel):

    name: str

    age: int = Field(gt=0)

    gender: str

    contact_number: str

    family_members: int = Field(ge=0)

    camp_id: int


class VictimUpdate(BaseModel):

    name: str

    age: int = Field(gt=0)

    gender: str

    contact_number: str

    family_members: int = Field(ge=0)

    camp_id: int


class VictimResponse(VictimCreate):

    id: int

    class Config:
        from_attributes = True
