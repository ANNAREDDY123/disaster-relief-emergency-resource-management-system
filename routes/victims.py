from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.camp import Camp
from models.victim import Victim
from schemas.victim import VictimCreate, VictimUpdate
from services.relief_service import (
    has_available_capacity,
    update_capacity_on_registration
)

router = APIRouter(
    prefix="/victims",
    tags=["Victims"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def register_victim(
    victim: VictimCreate,
    db: Session = Depends(get_db)
):

    camp = db.query(Camp).filter(
        Camp.id == victim.camp_id
    ).first()

    if not camp:
        raise HTTPException(
            status_code=404,
            detail="Camp not found."
        )

    if not has_available_capacity(camp):
        raise HTTPException(
            status_code=400,
            detail="Camp is full."
        )

    db_victim = Victim(**victim.model_dump())

    db.add(db_victim)

    update_capacity_on_registration(camp)

    db.commit()
    db.refresh(db_victim)

    return db_victim


@router.get("/")
def get_victims(
    camp_id: int = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Victim)

    if camp_id:
        query = query.filter(
            Victim.camp_id == camp_id
        )

    total = query.count()

    victims = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": victims
    }


@router.get("/{victim_id}")
def get_victim(
    victim_id: int,
    db: Session = Depends(get_db)
):

    victim = db.query(Victim).filter(
        Victim.id == victim_id
    ).first()

    if not victim:
        raise HTTPException(
            status_code=404,
            detail="Victim not found."
        )

    return victim


@router.put("/{victim_id}")
def update_victim(
    victim_id: int,
    victim: VictimUpdate,
    db: Session = Depends(get_db)
):

    db_victim = db.query(Victim).filter(
        Victim.id == victim_id
    ).first()

    if not db_victim:
        raise HTTPException(
            status_code=404,
            detail="Victim not found."
        )

    for key, value in victim.model_dump().items():
        setattr(db_victim, key, value)

    db.commit()
    db.refresh(db_victim)

    return db_victim
