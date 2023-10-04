from pydantic import BaseModel
from datetime import datetime


class EnrollmentStudyBase(BaseModel):
    lead_id: int
    career_id: int
    subject_id: int
    times_enrolled: int


class EnrollmentStudyCreateSchema(EnrollmentStudyBase):
    pass


class EnrollmentStudySchema(EnrollmentStudyBase):
    id: int

    class Config:
        orm_mode = True
