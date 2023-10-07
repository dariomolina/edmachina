from pydantic import BaseModel


class SubjectsBase(BaseModel):
    name: str
    study_duration: int
    career_id: int


class SubjectsCreateSchema(SubjectsBase):
    pass


class SubjectsSchema(SubjectsBase):
    id: int

    class Config:
        from_attributes = True
