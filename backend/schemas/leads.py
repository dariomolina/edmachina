from pydantic import BaseModel
from datetime import datetime


class LeadBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    address: str = None
    phone: str = None


class LeadCreateSchema(LeadBaseSchema):
    pass


class LeadSchema(LeadBaseSchema):
    id: int

    class Config:
        orm_mode = True
