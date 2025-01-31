# FastAPI-LangChain-QA-Manager

A modern web application built with **FastAPI** that combines **AI-powered** question answering with a **PostgreSQL** database backend.

## ✨ Key Features
- 🚀 RESTful API endpoints built with `FastAPI` for high performance and async support
- 🗄️ PostgreSQL database integration using `SQLAlchemy ORM`
- 🤖 AI-powered question answering using `LangChain` and `OpenAI's GPT` models
- ⚡ CRUD operations for managing questions and answers
- 📚 Automatic API documentation with `OpenAPI/Swagger UI`

## 🛠️ Tech Stack
- **FastAPI**: Modern, fast web framework for building APIs
- **PostgreSQL**: Robust relational database for data persistence
- **SQLAlchemy**: Powerful SQL toolkit and ORM for Python
- **LangChain**: Framework for developing applications powered by language models
- **OpenAI**: State-of-the-art GPT models for natural language processing
- **Pydantic**: Data validation using Python type annotations

## 🎯 Application Features
The application enables users to:
1. 📝 Create and manage questions and answers
2. 🤖 Generate AI-powered responses using OpenAI's language models
3. 💾 Store and retrieve QA pairs from PostgreSQL database
4. 🔄 Perform full CRUD operations through RESTful endpoints

---

## 🚀 Getting Started

### Prerequisites
1. **PostgreSQL Server**
   - Download and register server on PostgreSQL
   - Configure database connection in `database.py`

2. **OpenAI API Key**
   - Create an OpenAI API key
   - Add it to `langchain_answers.py`

### Installation
1. Install dependencies:
   ```bash
   # Import all directories from pyproject.toml
   poetry install
   ```

2. Navigate to project directory:
   ```bash
   cd FastAPIApplication
   ```

3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

4. View API documentation:
   - Open your browser and go to `http://127.0.0.1:8000/docs`
   - Interactive Swagger UI will be available for testing endpoints
   - Inside the `caller.ipynb` you can also call endpoints through the local session

---

## 📝 Notes
- Ensure all environment variables are properly set
- Check database connection before starting the application
- Make sure OpenAI API key is valid and has sufficient credits
