from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Institution
from app.schemas import InstitutionRead

router = APIRouter(prefix="/api/v1/institutions", tags=["institutions"])


@router.get("", response_model=list[InstitutionRead])
def list_institutions(db: Session = Depends(get_db)):
    return db.query(Institution).order_by(Institution.name).all()


@router.get("/{institution_id}", response_model=InstitutionRead)
def get_institution(institution_id: str, db: Session = Depends(get_db)):
    inst = db.query(Institution).filter(Institution.id == institution_id).first()
    if not inst:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Institution not found")
    return inst
