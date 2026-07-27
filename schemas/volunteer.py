from pydantic import BaseModel, EmailStr


class VolunteerCreate(BaseModel):

    name: str

    email: EmailStr

    phone: str

    assigned_camp: int | None = None

    availability_status: bool = True


class VolunteerAssign(BaseModel):

    camp_id: int


class VolunteerResponse(VolunteerCreate):

    id: int

    class Config:
        from_attributes = True
