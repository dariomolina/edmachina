from sqlalchemy.orm import Session

from models.academic import Subjects, Career
from models.enrollment import EnrollmentStudy
from models.leads import Lead
from schemas.enrollment_study import EnrollmentStudyCreateSchema, EnrollmentStudyListSchema


def create_enrollment_study(
        session: Session,
        enrollment_study: EnrollmentStudyCreateSchema
):
    db_enrollment_study = EnrollmentStudy(**enrollment_study.dict())
    session.add(db_enrollment_study)
    session.commit()
    session.refresh(db_enrollment_study)
    session.close()
    return db_enrollment_study


def get_enrollment_study(session: Session, skip, limit):
    enrollments_study = session.query(
        EnrollmentStudy.id,
        Lead.first_name,
        Lead.last_name,
        Lead.dni,
        Career.name,
        Subjects.name,
        EnrollmentStudy.registration_date,
    ).join(
        Lead, EnrollmentStudy.lead_id == Lead.id,
    ).join(
        Subjects,
        EnrollmentStudy.subject_id == Subjects.id,
    ).join(
        Career,
        Subjects.career_id == Career.id,
    ).order_by(EnrollmentStudy.registration_date.desc()).offset(skip).limit(limit).all()
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


def enrollment_study_count(session: Session):
    enrollment_count = session.query(EnrollmentStudy).count()
    return enrollment_count
