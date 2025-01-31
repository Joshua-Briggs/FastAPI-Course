from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database import session_local
from models import QAA

router = APIRouter(prefix='/qaa', tags=['qaa'])
# creating our own "sub-application" and using a unique 
# prefix and tag to add it's own endpoints in the program

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
# this function will check to make sure that there is a active session

db_dependency = Annotated[Session, Depends(get_db)]
# allows us to replicate this into all the functions 
# and communicate into our database

class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=500)
class AnswerRequest(BaseModel):
    answer: str = Field(min_length=1, max_length=500)
# we create classes and attach the pydantic "BaseModel" to 
# use the field operations this allows us to create 
# safeguards on the data the user may enter into our application

GET_ALL_DESCRIPTION = """
Returns all questions and answers from the database.
Uses the .all() method to retrieve every record in the QAA table.
Returns an empty list if no records exist.
"""

@router.get("/get-all-qaa", 
            status_code=status.HTTP_200_OK,
            description=GET_ALL_DESCRIPTION)
async def get_all_qaa(db: db_dependency):
    qaa_list = db.query(QAA).all()
    return qaa_list
# this function has a "get" endpoint, this means the function should return data

GET_BY_ID_DESCRIPTION = """
Returns a specific question and answer by its ID.
Uses .first() to efficiently retrieve the single matching record.
Returns 404 if no matching record is found.
"""

@router.get("/get-qaa-by-id/{qaa_id}", 
            status_code=status.HTTP_200_OK,
            description=GET_BY_ID_DESCRIPTION)
async def get_qaa(db: db_dependency, qaa_id: int = Path(gt=0)):
    qaa = db.query(QAA).filter(QAA.id == qaa_id).first()
    if qaa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question and answer not found')
    return qaa
# our first function has a "get" endpoint, this means the function should return data

CREATE_DESCRIPTION = """
Creates a new question in the database with an empty answer.
Validates the question length (1-500 characters).
Returns the created QAA object with its assigned ID.
"""

@router.post("/create-question", 
             status_code=status.HTTP_201_CREATED,
             description=CREATE_DESCRIPTION)
async def create_question(db: db_dependency, question_request: QuestionRequest):
    qaa = QAA(
        question=question_request.question,
        answer=""  # Initially empty answer
    )
    db.add(qaa)
    db.commit()
    db.refresh(qaa)
    return qaa
# this function has a "post" endpoint, this means the function should create data

UPDATE_ANSWER_DESCRIPTION = """
Updates the answer for a specific question by ID.
Validates the answer length (1-500 characters).
Returns 404 if the question ID is not found.
Returns the updated QAA object.
"""

@router.put("/edit-qaa-by-id/{qaa_id}/answer", 
            status_code=status.HTTP_204_NO_CONTENT,
            description=UPDATE_ANSWER_DESCRIPTION)
async def update_answer(db: db_dependency, 
                       answer_request: AnswerRequest, 
                       qaa_id: int = Path(gt=0)):
    qaa = db.query(QAA).filter(QAA.id == qaa_id).first()
    if qaa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question and answer not found')
    
    qaa.answer = answer_request.answer
    db.commit()
    return qaa
# this function has a "put" endpoint, this means the function should edit data

UPDATE_QUESTION_DESCRIPTION = """
Updates the question text for a specific QAA by ID.
Validates the question length (1-500 characters).
Returns 404 if the question ID is not found.
Returns the updated QAA object.
"""

@router.put("/edit-qaa-by-id/{qaa_id}/question", 
            status_code=status.HTTP_204_NO_CONTENT,
            description=UPDATE_QUESTION_DESCRIPTION)
async def update_question(db: db_dependency, 
                         question_request: QuestionRequest, 
                         qaa_id: int = Path(gt=0)):
    qaa = db.query(QAA).filter(QAA.id == qaa_id).first()
    if qaa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question and answer not found')
    
    qaa.question = question_request.question
    db.commit()
    return qaa
# this function has a "put" endpoint, this means the function should edit data

DELETE_BY_ID_DESCRIPTION = """
Deletes a specific question and answer by ID.
Returns 404 if the question ID is not found.
Returns no content on successful deletion.
"""

@router.delete("/delete-qaa-by-id/{qaa_id}", 
               status_code=status.HTTP_204_NO_CONTENT,
               description=DELETE_BY_ID_DESCRIPTION)
async def delete_qaa(db: db_dependency, qaa_id: int = Path(gt=0)):
    qaa = db.query(QAA).filter(QAA.id == qaa_id).first()
    if qaa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question and answer not found')
    
    db.delete(qaa)
    db.commit()
    return None
# this function has a "delete" endpoint, this means the function should remove data

DELETE_ALL_DESCRIPTION = """
Deletes all questions and answers from the database.
This operation cannot be undone.
Returns no content on successful deletion.
"""

@router.delete("/delete-all-qaa", 
               status_code=status.HTTP_204_NO_CONTENT,
               description=DELETE_ALL_DESCRIPTION)
async def delete_all_qaa(db: db_dependency):
    db.query(QAA).delete()
    db.commit()
    return None
# this function has a "delete" endpoint, this means the function should remove data