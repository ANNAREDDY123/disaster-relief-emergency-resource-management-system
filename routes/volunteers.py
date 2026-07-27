  from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.camp import Camp
from models.volunteer import Volunteer
from schemas.volunteer import VolunteerCreate
from services.relief_service import (
    duplicate_email_exists,
    volunteer_can_be_assigned
)

router = APIRouter(
    prefix="/volunteers",
    tags=["Volunteers"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_volunteer(
    volunteer: VolunteerCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Volunteer).filter(
        Volunteer.email == volunteer.email
    ).first()

    if duplicate_email_exists(existing):
        raise HTTPException(
            status_code=400,
            detail="Email already exists."
        )

    db_volunteer = Volunteer(**volunteer.model_dump())

    db.add(db_volunteer)
    db.commit()
    db.refresh(db_volunteer)

    return db_volunteer


@router.get("/")
def get_volunteers(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Volunteer)

    total = query.count()

    volunteers = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": volunteers
    }


@router.post("/{volunteer_id}/assign/{camp_id}")
def assign_volunteer(
    volunteer_id: int,
    camp_id: int,
    db: Session = Depends(get_db)
):

    volunteer = db.query(Volunteer).filter(
        Volunteer.id == volunteer_id
    ).first()

    if not volunteer:
        raise HTTPException(
            status_code=404,
            detail="Volunteer not found."
        )

    camp = db.query(Camp).filter(
        Camp.id == camp_id
    ).first()

    if not camp:
        raise HTTPException(
            status_code=404,
            detail="Camp not found."
        )

    if not volunteer_can_be_assigned(volunteer):
        raise HTTPException(
            status_code=400,
            detail="Volunteer is already assigned to an active camp."
        )

    volunteer.assigned_camp = camp_id
    volunteer.availability_status = False

    db.commit()
    db.refresh(volunteer)

    return {
        "message": "Volunteer assigned successfully.",
        "data": volunteer
    }


@router.get("/assignments/all")
def volunteer_assignments(
    db: Session = Depends(get_db)
):

    return db.query(Volunteer).all()
