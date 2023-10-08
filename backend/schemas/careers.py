from pydantic import BaseModel


class CareerBaseSchema(BaseModel):
    name: str


class CareerCreateSchema(CareerBaseSchema):
    study_duration: int


class CareerSchema(CareerBaseSchema):
    id: int
    study_duration: int

    class Config:
        from_attributes = True


class CareerSelectSchema(CareerBaseSchema):
    id: int

    class Config:
        from_attributes = True
