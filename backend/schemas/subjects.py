from pydantic import BaseModel


class SubjectsBase(BaseModel):
    name: str
    study_duration: int
    carrera_id: int


class SubjectsCreateSchema(SubjectsBase):
    pass


class SubjectsSchema(SubjectsBase):
    id: int

    class Config:
        orm_mode = True
