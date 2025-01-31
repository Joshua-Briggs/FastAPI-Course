from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from langchain_openai import ChatOpenAI
from sqlalchemy.orm import Session

from database import session_local
from models import QAA

# OpenAI configuration
OPENAI_API_KEY = ""

llm = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0.0,
    openai_api_key=OPENAI_API_KEY
)

router = APIRouter(prefix='/langchain', tags=['langchain'])
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

GET_AI_ANSWER_DESC = """
    Updates a QAA (Question and Answer) entry with an AI-generated answer.
    
    Parameters:
    - db: Database session dependency
    - qaa_id: ID of the question to answer (must be greater than 0)
    
    Returns:
    - QAA object with the updated AI answer
    
    Raises:
    - 401 Unauthorized: If the OpenAI API key is invalid
    - 404 Not Found: If the question ID doesn't exist
    - 500 Internal Server Error: If there's an error with the OpenAI API
    """

@router.put("/{qaa_id}/ai-answer", status_code=status.HTTP_200_OK, description=GET_AI_ANSWER_DESC)
async def get_ai_answer(db: db_dependency, qaa_id: int = Path(gt=0)):
    # First check if the API key is valid/working
    if not OPENAI_API_KEY or OPENAI_API_KEY.startswith('sk-') is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid or missing OpenAI API key'
        )

    qaa = db.query(QAA).filter(QAA.id == qaa_id).first()
    if qaa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question and answer not found')
    
    try:
        # Get AI response
        result = llm.invoke(qaa.question)
        
        # Extract the content from the AI message
        answer_content = result.content
        
        # Update the answer in the database
        qaa.answer = answer_content
        db.commit()
        
        qaa = db.query(QAA).filter(QAA.id == qaa_id).first()
        return qaa
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error with OpenAI API: {str(e)}'
        )