
from sqlalchemy.orm import Session

from models.academic import Career
from schemas.careers import CareerCreateSchema


def create_career(session: Session, career: CareerCreateSchema):
    db_career = Career(**career.dict())
    session.add(db_career)
    session.commit()
    session.refresh(db_career)
    session.close()
    return db_career
