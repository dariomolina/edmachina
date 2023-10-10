from datetime import datetime
from typing import List

from pydantic import BaseModel


class EnrollmentStudyBase(BaseModel):
    lead_id: int
    career_id: int
    subject_id: int


class EnrollmentStudyCreateSchema(EnrollmentStudyBase):
    pass


class EnrollmentStudySchema(EnrollmentStudyBase):
    id: int
    registration_date: datetime

    class Config:
        from_attributes = True


class EnrollmentStudyListSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    dni: int
    career_name: str
    subject_name: str
    registration_date: datetime


class EnrollmentStudyPaginationSchema(BaseModel):
    items: List[EnrollmentStudyListSchema]
    count: int
