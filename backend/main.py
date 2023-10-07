import json
from typing import Dict, List

from fastapi import FastAPI, Request, Body, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.orm import Session

from models import users as user_model
from models.academic import Career, Subjects
from models.enrollment import EnrolledProgram, EnrollmentStudy
from models.leads import Lead
from schemas.careers import CareerCreateSchema, CareerSchema
from schemas.enrolled_program import EnrolledProgramSchema, EnrolledProgramCreateSchema
from schemas.enrollment_study import EnrollmentStudyCreateSchema, EnrollmentStudySchema
from schemas.leads import LeadCreateSchema, LeadSchema
from schemas.subjects import SubjectsSchema, SubjectsCreateSchema
from schemas.users import UserSchema, CreateUserSchema, UserLoginSchema
from services.db import users as user_db_services
from settings import get_db

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["http://localhost:3000"], # Add your frontend origin here
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
 )


@app.post('/signup', response_model=UserSchema)
def signup(
    payload: CreateUserSchema = Body(),
    session: Session = Depends(get_db)
):
    """Processes request to register user account."""
    payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
    return user_db_services.create_user(session, user=payload)


@app.post('/login', response_model=Dict)
def login(
    payload: UserLoginSchema = Body(),
    session: Session = Depends(get_db)
):
    """Processes user's authentication and returns a token
    on successful authentication.

    request body:

    - username: Unique identifier for a user 'e.g' email,
                phone number, name

    - password:
    """
    try:
        user: user_model.User = user_db_services.get_user(
            session=session, email=payload.email
        )
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    is_validated: bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    return user.generate_token()


@app.post("/career/")
async def create_career(
    request: Request,
    session: Session = Depends(get_db)
):
    try:
        raw_data = await request.body()
        data_str = raw_data.decode("utf-8")
        data_dict = json.loads(data_str)
        career = CareerCreateSchema(**data_dict)
        db_career = Career(**career.dict())
        session.add(db_career)
        session.commit()
        session.refresh(db_career)
        session.close()

    except json.JSONDecodeError as json_error:
        raise HTTPException(
            status_code=400,
            detail=str(json_error)
        )

    except ValueError as validation_error:
        raise HTTPException(
            status_code=422,  # Unprocessable Entity
            detail=str(validation_error)
        )

    except IntegrityError as db_error:
        raise HTTPException(
            status_code=500,  # Internal Server Error
            detail=str(db_error.detail)
        )

    return {"message": "Carrera creada exitosamente"}


@app.get("/career/", response_model=List[CareerSchema])
def get_careers(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    careers = session.query(Career).offset(skip).limit(limit).all()
    return careers


@app.post("/subject/", response_model=SubjectsSchema)
def create_subject(subject: SubjectsCreateSchema, session: Session = Depends(get_db)):
    try:
        db_subject = Subjects(**subject.dict())
        session.add(db_subject)
        session.commit()
        session.refresh(db_subject)
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error.detail
        )
    return db_subject


@app.get("/subjects/", response_model=List[SubjectsSchema])
def get_subjects(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    subjects = session.query(Subjects).offset(skip).limit(limit).all()
    return subjects


@app.post("/leads/")
def create_lead(
    lead: LeadCreateSchema,
    session: Session = Depends(get_db)
):
    try:
        db_lead = Lead(**lead.dict())
        session.add(db_lead)
        session.commit()
        session.refresh(db_lead)
        session.close()
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error.detail
        )
    return db_lead


@app.get("/leads/", response_model=List[LeadSchema])
def get_leads(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    leads = session.query(Lead).offset(skip).limit(limit).all()
    session.close()
    return leads


@app.get("/leads/{lead_id}")
def read_lead(
    lead_id: int,
    session: Session = Depends(get_db)
):
    lead = session.query(Lead).filter(Lead.id == lead_id).first()
    session.close()
    return lead


@app.post("/enrolled_program/", response_model=EnrolledProgramSchema)
async def create_enrolled_program(
    enrolled_program: EnrolledProgramCreateSchema,
    session: Session = Depends(get_db)
):
    try:
        db_enrolled_program = EnrolledProgram(**enrolled_program.dict())
        session.add(db_enrolled_program)
        session.commit()
        session.refresh(db_enrolled_program)
        session.close()
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error.detail
        )


@app.post("/enrollment-study/", response_model=EnrollmentStudySchema)
async def create_enrollment_study(
    enrollment_study: EnrollmentStudyCreateSchema,
    session: Session = Depends(get_db),
):
    try:
        db_enrollment_study = EnrollmentStudy(**enrollment_study.dict())
        session.add(db_enrollment_study)
        session.commit()
        session.refresh(db_enrollment_study)
        session.close()
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error.detail
        )
    return db_enrollment_study
