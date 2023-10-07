from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)

from settings import Base


class Career(Base):
    __tablename__ = 'career'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    study_duration = Column(Integer)


class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    study_duration = Column(Integer)  # tiempo de cursado
    career_id = Column(Integer, ForeignKey('career.id'), nullable=False)
