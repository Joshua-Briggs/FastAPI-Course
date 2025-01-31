from fastapi import FastAPI
from routers import questions_and_answers, langchain_answers
import models
from database import engine

APP_DESCRIPTION = """
A modern web application built with FastAPI that combines AI-powered question answering with a PostgreSQL database backend.

Key Features:
- RESTful API endpoints built with FastAPI for high performance and async support
- PostgreSQL database integration using SQLAlchemy ORM
- AI-powered question answering using LangChain and OpenAI's GPT models
- CRUD operations for managing questions and answers
- Automatic API documentation with OpenAPI/Swagger UI

Tech Stack:
- FastAPI: Modern, fast web framework for building APIs
- PostgreSQL: Robust relational database for data persistence
- SQLAlchemy: Powerful SQL toolkit and ORM for Python
- LangChain: Framework for developing applications powered by language models
- OpenAI: State-of-the-art GPT models for natural language processing
- Pydantic: Data validation using Python type annotations

The application allows users to:
1. Create and manage questions and answers
2. Generate AI-powered responses using OpenAI's language models
3. Store and retrieve QA pairs from a PostgreSQL database
4. Perform full CRUD operations through RESTful endpoints
"""

app = FastAPI(
    title="FastAPI-LangChain-QA-Manager",
    description=APP_DESCRIPTION,
    version="0.0.1"
)
# initilizing our application

models.base.metadata.create_all(bind=engine)
# Create database tables based on the models

app.include_router(router=questions_and_answers.router)
app.include_router(router=langchain_answers.router)
# including our routers (in this case only two), to the application