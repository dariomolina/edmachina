from pydantic import BaseModel


class EnrolledProgramBase(BaseModel):
    lead_id: int
    career_id: int


class EnrolledProgramCreateSchema(EnrolledProgramBase):
    pass


class EnrolledProgramSchema(EnrolledProgramBase):
    id: int

    class Config:
        from_attributes = True
