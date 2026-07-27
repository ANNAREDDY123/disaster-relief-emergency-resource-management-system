from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.camp import Camp
from schemas.camp import CampCreate, CampUpdate
from services.relief_service import valid_camp_status

router = APIRouter(
    prefix="/camps",
    tags=["Relief Camps"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_camp(
    camp: CampCreate,
    db: Session = Depends(get_db)
):

    if not valid_camp_status(camp.status):
        raise HTTPException(
            status_code=400,
            detail="Invalid camp status."
        )

    db_camp = Camp(**camp.model_dump())

    db.add(db_camp)
    db.commit()
    db.refresh(db_camp)

    return db_camp


@router.get("/")
def get_camps(
    district: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Camp)

    if district:
        query = query.filter(
            Camp.district == district
        )

    total = query.count()

    camps = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": camps
    }


@router.get("/{camp_id}")
def get_camp(
    camp_id: int,
    db: Session = Depends(get_db)
):

    camp = db.query(Camp).filter(
        Camp.id == camp_id
    ).first()

    if not camp:
        raise HTTPException(
            status_code=404,
            detail="Camp not found."
        )

    return camp


@router.put("/{camp_id}")
def update_camp(
    camp_id: int,
    camp: CampUpdate,
    db: Session = Depends(get_db)
):

    db_camp = db.query(Camp).filter(
        Camp.id == camp_id
    ).first()

    if not db_camp:
        raise HTTPException(
            status_code=404,
            detail="Camp not found."
        )

    for key, value in camp.model_dump().items():
        setattr(db_camp, key, value)

    db.commit()
    db.refresh(db_camp)

    return db_camp


@router.delete("/{camp_id}")
def delete_camp(
    camp_id: int,
    db: Session = Depends(get_db)
):

    camp = db.query(Camp).filter(
        Camp.id == camp_id
    ).first()

    if not camp:
        raise HTTPException(
            status_code=404,
            detail="Camp not found."
        )

    db.delete(camp)
    db.commit()

    return {
        "message": "Camp deleted successfully."
    }
