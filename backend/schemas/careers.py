from pydantic import BaseModel


class CareerBase(BaseModel):
    name: str
    study_duration: int


class CareerCreateSchema(CareerBase):
    pass


class CareerSchema(CareerBase):
    id: int

    class Config:
        from_attributes = True
