from sqlalchemy.orm import Session

from models.academic import Subjects, Career
from schemas.subjects import SubjectsCreateSchema, SubjectCareerSchema


def create_subject(session: Session, subject: SubjectsCreateSchema):
    db_subject = Subjects(**subject.dict())
    session.add(db_subject)
    session.commit()
    session.refresh(db_subject)
    session.close()
    return db_subject


def get_subjects_by_careers(session: Session, skip, limit):
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
    return result

