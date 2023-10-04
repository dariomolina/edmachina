from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Boolean,
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
    carrera_id = Column(Integer, ForeignKey('career.id'), nullable=False)


class EnrollmentStudy(Base):
    __tablename__ = 'enrollment_study'
    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey('lead.id'), nullable=False)
    career_id = Column(Integer, ForeignKey('career.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    times_enrolled = Column(Integer)  # veces cursado
    registration_date = Column(DateTime, default=datetime.utcnow)
    approved = Column(Boolean, default=False)
