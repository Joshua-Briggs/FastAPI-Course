from fastapi import FastAPI
from routers import questions_and_answers, langchain_answers
import models
from database import engine

app = FastAPI()
# initilizing our application

models.base.metadata.create_all(bind=engine)
# Create database tables based on the models

app.include_router(router=questions_and_answers.router)
app.include_router(router=langchain_answers.router)
# including our routers (in this case only two), to the application