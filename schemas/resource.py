from datetime import date
from pydantic import BaseModel, Field


class ResourceCreate(BaseModel):

    camp_id: int

    resource_type: str

    quantity: int = Field(gt=0)

    distributed_by: str

    distribution_date: date


class ResourceResponse(ResourceCreate):

    id: int

    class Config:
        from_attributes = True
