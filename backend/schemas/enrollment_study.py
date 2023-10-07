from pydantic import BaseModel


class EnrollmentStudyBase(BaseModel):
    enrolled_program_id: int
    subject_id: int


class EnrollmentStudyCreateSchema(EnrollmentStudyBase):
    pass


class EnrollmentStudySchema(EnrollmentStudyBase):
    id: int

    class Config:
        from_attributes = True
