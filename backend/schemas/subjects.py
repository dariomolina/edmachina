from pydantic import BaseModel


class SubjectsCreateSchema(BaseModel):
    name: str
    career_id: int
    study_duration: int


class SubjectsSchema(BaseModel):
    id: int
    name: str
    career_id: int
    study_duration: int

    class Config:
        from_attributes = True


class SubjectsListSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class SubjectCareerSchema(SubjectsListSchema):
    career_name: str
    study_duration: int

    class Config:
        from_attributes = True
