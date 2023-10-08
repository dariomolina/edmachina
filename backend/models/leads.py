from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

from settings import Base


class Lead(Base):
    __tablename__ = 'lead'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dni = Column(Integer, unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    address = Column(String)
    phone = Column(String)
    registration_date = Column(DateTime, default=datetime.utcnow)
