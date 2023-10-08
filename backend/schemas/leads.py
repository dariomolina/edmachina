from datetime import datetime

from pydantic import BaseModel


class LeadBaseSchema(BaseModel):
    first_name: str
    last_name: str
    dni: int
    email: str
    address: str = None
    phone: str = None


class LeadCreateSchema(LeadBaseSchema):
    pass


class LeadSchema(LeadBaseSchema):
    id: int
    registration_date: datetime

    class Config:
        from_attributes = True


class LeadListSchema(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True
