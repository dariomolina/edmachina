from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    Boolean,
)

from settings import Base


class EnrollmentStudy(Base):
    __tablename__ = 'enrollment_study'
    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey('lead.id'), nullable=False)
    career_id = Column(Integer, ForeignKey('career.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    registration_date = Column(DateTime, default=datetime.utcnow)
