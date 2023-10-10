import json
from typing import List

from fastapi import FastAPI, Request, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from models.academic import Career, Subjects
from models.leads import Lead
from schemas.careers import CareerCreateSchema, CareerSchema, CareerSelectSchema
from schemas.enrollment_study import EnrollmentStudyCreateSchema, EnrollmentStudyListSchema
from schemas.leads import LeadCreateSchema, LeadSchema, LeadListSchema
from schemas.subjects import SubjectsCreateSchema, SubjectsListSchema, SubjectCareerSchema
from services.db.careers import create_career
from services.db.enrollment_study import create_enrollment_study, get_enrollment_study
from services.db.leads import create_lead, get_leads_selector
from services.db.subjects import create_subject, get_subjects_by_careers
from settings import get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend origin here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/career/", response_model=int)
async def post_create_career(
    request: Request,
    career: CareerCreateSchema,
    session: Session = Depends(get_db)
):
    """
    Create a new academic career.

    Args:
        request (Request): The HTTP request.
        career (CareerCreateSchema): The data of the career to create.
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        int: The ID of the created career.
    """
    try:
        db_career = create_career(session, career=career)
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

    return db_career.id


@app.get("/career/", response_model=List[CareerSchema])
def get_careers(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    """
    Get a list of academic careers.

    Args:
        skip (int, optional): The number of records to skip. Defaults to 0.
        limit (int, optional): The maximum number of records to return. Defaults to 10.
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[CareerSchema]: The list of academic careers.
    """
    careers = session.query(Career).offset(skip).limit(limit).all()
    return careers


@app.get("/select-careers/", response_model=List[CareerSelectSchema])
def get_select_careers(session: Session = Depends(get_db)):
    """
    Get a list of academic careers for selection.

    Args:
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[CareerSelectSchema]: The list of academic careers for selection.
    """
    careers = session.query(Career.id, Career.name).all()
    careers = [
        CareerSelectSchema(id=int(_id), name=name) for _id, name in careers
    ]
    return careers


@app.post("/subject-create/", response_model=int)
async def post_create_subject(
    request: Request,
    subject: SubjectsCreateSchema,
    session: Session = Depends(get_db)
):
    """
    Endpoint for subject creation.

    Args:
        request (Request): The HTTP request.
        subject (SubjectsCreateSchema): The data for the subject to be created.
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        int: The ID of the created subject.
    """
    try:
        db_subject = create_subject(session, subject=subject)
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
    return db_subject.id


@app.get("/subjects_with_careers/", response_model=List[SubjectCareerSchema])
def get_subjects_with_careers(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_db)
):
    """
    Get a list of subjects with associated academic careers.

    Args:
        skip (int, optional): The number of records to skip. Defaults to 0.
        limit (int, optional): The maximum number of records to return. Defaults to 10.
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[SubjectCareerSchema]: The list of subjects with associated academic careers.
    """
    try:
        subjects_with_careers = get_subjects_by_careers(session, skip=skip, limit=limit)
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
    return subjects_with_careers


@app.get("/select-subjects/{career_id}", response_model=List[SubjectsListSchema])
def get_select_subjects(
    career_id: int,
    session: Session = Depends(get_db)
):
    """
    Get a list of subjects for selection within a specific academic career.

    Args:
        career_id (int): The ID of the academic career.
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[SubjectsListSchema]: The list of subjects available for selection.
    """
    subjects = session.query(Subjects.id, Subjects.name).filter(Subjects.career_id == career_id)
    subjects = [
        SubjectsListSchema(id=int(_id), name=name) for _id, name in subjects
    ]
    return subjects


@app.post("/leads/", response_model=int)
async def post_create_lead(
    request: Request,
    lead: LeadCreateSchema,
    session: Session = Depends(get_db)
):
    """
    Create a new lead or prospective student.

    Args:
        request (Request): The HTTP request.
        lead (LeadCreateSchema): The data for the lead to be created.
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        int: The ID of the created lead.
    """
    try:
        db_lead = create_lead(session, lead=lead)
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
    return db_lead.id


@app.get("/leads/", response_model=List[LeadSchema])
def get_lead(
    session: Session = Depends(get_db),
):
    """
    Get a list of leads or prospective students.

    Args:
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[LeadSchema]: The list of leads or prospective students.
    """
    lead = session.query(Lead).all()
    return lead


@app.get("/select-leads/", response_model=List[LeadListSchema])
def find_leads(
    session: Session = Depends(get_db)
):
    """
    Find leads or prospective students for selection.

    Args:
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[LeadListSchema]: The list of leads or prospective students for selection.
    """
    leads = get_leads_selector(session)
    return leads


@app.post("/enrollment-study/", response_model=int)
async def post_create_enrollment_study(
    request: Request,
    enrollment_study: EnrollmentStudyCreateSchema,
    session: Session = Depends(get_db),
):
    """
    Create a new enrollment study record.

    Args:
        request (Request): The HTTP request.
        enrollment_study (EnrollmentStudyCreateSchema): The data for the enrollment study record to be created.
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        int: The ID of the created enrollment study record.
    """
    try:
        db_enrollment_study = create_enrollment_study(
            session,
            enrollment_study=enrollment_study
        )
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
    return db_enrollment_study.id


@app.get("/enrollment-study/", response_model=List[EnrollmentStudyListSchema])
def find_enrollment_study(
    session: Session = Depends(get_db),
):
    """
    Get a list of enrollment study records.

    Args:
        session (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[EnrollmentStudyListSchema]: The list of enrollment study records.
    """
    enrollments_study = get_enrollment_study(session)
    return enrollments_study
