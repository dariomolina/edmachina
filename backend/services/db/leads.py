from sqlalchemy.orm import Session

from models.leads import Lead
from schemas.leads import LeadCreateSchema, LeadListSchema


def create_lead(session: Session, lead: LeadCreateSchema):
    db_lead = Lead(**lead.dict())
    session.add(db_lead)
    session.commit()
    session.refresh(db_lead)
    session.close()
    return db_lead


def get_leads_selector(session: Session):
    leads = session.query(Lead.id, Lead.first_name, Lead.last_name).all()
    leads = [
        LeadListSchema(
            id=int(_id),
            first_name=first_name,
            last_name=last_name
        ) for _id, first_name, last_name in leads
    ]
    session.close()
    return leads
