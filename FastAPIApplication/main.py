from fastapi import FastAPI
from .routers import questions_and_answers
import models

app = FastAPI()
# initilizing our application

models.Base.metadata.create_all(bind=models.engine)
# Create database tables based on the models

app.include_router(router=questions_and_answers.router)
# including our routers (in this case only one), to the application