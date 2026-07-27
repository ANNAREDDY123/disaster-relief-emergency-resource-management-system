from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.camp import Camp
from models.resource import Resource
from schemas.resource import ResourceCreate
from services.relief_service import valid_resource_quantity

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_resource(
    resource: ResourceCreate,
    db: Session = Depends(get_db)
):

    camp = db.query(Camp).filter(
        Camp.id == resource.camp_id
    ).first()

    if not camp:
        raise HTTPException(
            status_code=404,
            detail="Camp not found."
        )

    if not valid_resource_quantity(resource.quantity):
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than zero."
        )

    db_resource = Resource(**resource.model_dump())

    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)

    return db_resource


@router.get("/")
def get_resources(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Resource)

    total = query.count()

    resources = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": resources
    }


@router.get("/{resource_id}")
def get_resource(
    resource_id: int,
    db: Session = Depends(get_db)
):

    resource = db.query(Resource).filter(
        Resource.id == resource_id
    ).first()

    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found."
        )

    return resource


@router.get("/history/all")
def resource_history(
    db: Session = Depends(get_db)
):
    return db.query(Resource).all()
