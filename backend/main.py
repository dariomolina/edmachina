import json
from typing import Dict, List

from fastapi import FastAPI, Request, Body, Depends, HTTPException, status
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from models import users as user_model
from models.academic import Career, Subjects
from models.enrollment import EnrollmentStudy
from models.leads import Lead
from schemas.careers import CareerCreateSchema, CareerSchema, CareerSelectSchema
from schemas.enrollment_study import EnrollmentStudyCreateSchema, EnrollmentStudySchema, EnrollmentStudyListSchema
from schemas.leads import LeadCreateSchema, LeadSchema, LeadListSchema
from schemas.subjects import SubjectsSchema, SubjectsCreateSchema, SubjectsListSchema, SubjectCareerSchema
from schemas.users import UserSchema, CreateUserSchema, UserLoginSchema
from services.db import users as user_db_services
from settings import get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend origin here
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
            detail=str(db_error)
        )

    return {"message": "Carrera creada exitosamente"}


@app.get("/career/", response_model=List[CareerSchema])
def get_careers(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    careers = session.query(Career).offset(skip).limit(limit).all()
    return careers


@app.get("/select-careers/", response_model=List[CareerSelectSchema])
def get_select_subjects(session: Session = Depends(get_db)):
    """
    Endpoint usado para el selector de carreras, se envia [{id, name}]
    """
    careers = session.query(Career.id, Career.name).all()
    careers = [
        CareerSelectSchema(id=int(_id), name=name) for _id, name in careers
    ]
    return careers


@app.post("/subject-create/", response_model=SubjectsSchema)
async def create_subject(request: Request, session: Session = Depends(get_db)):
    """
    Endpoint para creacion de materia
    """
    try:
        raw_data = await request.body()
        data_str = raw_data.decode("utf-8")
        data_dict = json.loads(data_str)
        subject = SubjectsCreateSchema(**data_dict)
        db_subject = Subjects(**subject.dict())
        session.add(db_subject)
        session.commit()
        session.refresh(db_subject)
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
            detail=str(db_error)
        )
    return db_subject


@app.get("/subjects_with_careers/", response_model=List[SubjectCareerSchema])
def get_subjects_with_careers(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_db)
):
    try:
        subjects_with_careers = session.query(
            Subjects.id,
            Subjects.name,
            Subjects.study_duration,
            Career.name
        ).join(Career).offset(skip).limit(limit).all()

        result = []
        for _id, subject_name, study_duration, career_name in subjects_with_careers:
            subject = SubjectCareerSchema(
                id=_id,
                name=subject_name,
                study_duration=study_duration,
                career_name=career_name
            )
            result.append(subject)
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
    return result


@app.get("/select-subjects/{career_id}", response_model=List[SubjectsListSchema])
def get_select_subjects(
    career_id: int,
    session: Session = Depends(get_db)
):
    subjects = session.query(Subjects.id, Subjects.name).filter(Subjects.career_id == career_id)
    subjects = [
        SubjectsListSchema(id=int(_id), name=name) for _id, name in subjects
    ]
    return subjects


@app.post("/leads/")
async def create_lead(
    request: Request,
    session: Session = Depends(get_db)
):
    try:
        raw_data = await request.body()
        data_str = raw_data.decode("utf-8")
        data_dict = json.loads(data_str)
        lead = LeadCreateSchema(**data_dict)
        db_lead = Lead(**lead.dict())
        session.add(db_lead)
        session.commit()
        session.refresh(db_lead)
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
            detail=str(db_error)
        )
    return db_lead


@app.get("/leads/", response_model=List[LeadSchema])
def get_lead(
    session: Session = Depends(get_db),
):
    lead = session.query(Lead).all()
    session.close()
    return lead


@app.get("/select-leads/", response_model=List[LeadListSchema])
def find_leads(
    session: Session = Depends(get_db)
):
    leads = session.query(Lead.id, Lead.first_name, Lead.last_name).all()
    leads = [
        LeadListSchema(
            id=int(_id),
            first_name=first_name,
            last_name=last_name
        ) for _id, first_name, last_name in leads
    ]
    session.close()
    return leads


# @app.get("/leads/{lead_id}")
# def get_lead(
#     lead_id: int,
#     session: Session = Depends(get_db)
# ):
#     lead = session.query(Lead).filter(Lead.id == lead_id).first()
#     session.close()
#     return lead


@app.post("/enrollment-study/", response_model=EnrollmentStudySchema)
async def create_enrollment_study(
    request: Request,
    session: Session = Depends(get_db),
):
    try:
        raw_data = await request.body()
        data_str = raw_data.decode("utf-8")
        data_dict = json.loads(data_str)
        enrollment_study = EnrollmentStudyCreateSchema(**data_dict)
        db_enrollment_study = EnrollmentStudy(**enrollment_study.dict())
        session.add(db_enrollment_study)
        session.commit()
        session.refresh(db_enrollment_study)
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
            detail=str(db_error)
        )
    return db_enrollment_study


@app.get("/enrollment-study/", response_model=List[EnrollmentStudyListSchema])
def get_lead(
    session: Session = Depends(get_db),
):
    enrollments_study = session.query(
        EnrollmentStudy.id,
        Lead.first_name,
        Lead.last_name,
        Lead.dni,
        Career.name,
        Subjects.name,
        EnrollmentStudy.registration_date,
    ).join(
        Lead,
        EnrollmentStudy.lead_id == Lead.id,
    ).join(
        Subjects,
        EnrollmentStudy.subject_id == Subjects.id,
    ).join(
        Career,
        Subjects.career_id == Career.id,
    ).order_by(Lead.dni).all()
    enrollments_study = [
        EnrollmentStudyListSchema(
            id=_id,
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            career_name=career,
            subject_name=subject,
            registration_date=registration_date
        ) for _id, first_name, last_name, dni, career, subject, registration_date
        in enrollments_study
    ]
    session.close()
    return enrollments_study
