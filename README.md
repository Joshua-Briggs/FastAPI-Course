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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

> TO GET THIS APPLICATION RUNNING: 🏃‍♂️🏃‍♀️

--------------------------------------------------------------------------------------------------------

-> DOWNLOAD AND REGISTER SERVER ON POSTGRES 

--------------------------------------------------------------------------------------------------------

--> IMPLEMENT POSTGRES SERVER ONTO 'database.py' FILE 

--------------------------------------------------------------------------------------------------------

---> CREATE AN OPENAI API KEY AND ADD IT INSIDE THE 'langchain_answers.py' file 

--------------------------------------------------------------------------------------------------------

----> IMPORT ALL DIRECTORIES FROM PYPROJECT 

--------------------------------------------------------------------------------------------------------

-----> CD TO 'FastAPIApplication' DIRECTORY

--------------------------------------------------------------------------------------------------------

------> ONCE IN CORRECT LOCATION TYPE 'uvicorn main:app --reload'

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------------------------------------------------------------------------

-------> IF THE SERVER IS RUNNING GO TO 'http://127.0.0.1:8000/docs' TO VIEW ENDPOINTS 🎥

--------------------------------------------------------------------------------------------------------
