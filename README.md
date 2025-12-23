# FastAPI Echo Service

A simple and clean FastAPI project that demonstrates:
- Building RESTful endpoints
- Request validation with Pydantic
- Health check endpoint
- Writing automated tests with pytest
- Dependency management using Poetry

This project is suitable as a starter template or a learning example for FastAPI best practices.

---

## 🚀 Features

- **Echo endpoint**: Receives a text message and returns it as JSON
- **Health endpoint**: Returns server status and environment information
- **Modular structure** using routers and schemas
- **Automated tests** with pytest
- **Poetry-based** dependency management

---

## 📁 Project Structure

```
project/
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── echo.py
│       └── health.py
├── tests/
│   ├── test_echo.py
│   └── test_health.py
├── pyproject.toml
└── README.md
```

---

## 🛠 Requirements

- Python 3.10+
- Poetry

---

## 📦 Installation

1. Clone the repository
```
git clone <your-repo-url>
cd project
```

2. Install dependencies using Poetry
```
poetry install
```

3. Activate the virtual environment
```
poetry shell
```

---

## ▶️ Running the Application

Run the FastAPI app from the project root:
```
uvicorn app.main:app --reload
```

After starting the server, you can access:

- API documentation (Swagger):
  http://127.0.0.1:8000/docs

- Health check endpoint:
  http://127.0.0.1:8000/health

- Echo endpoint:
  POST http://127.0.0.1:8000/echo

Example request body:
```
{
  "message": "Hello FastAPI"
}
```

---

## 🧪 Running Tests

Tests are written using **pytest** and located in the `tests/` directory.

Run all tests with:
```
pytest -v
```

This will execute:
- Echo endpoint tests
- Health endpoint tests
- Request validation checks

---

## 🩺 Health Endpoint Details

The `/health` endpoint returns useful information for monitoring and deployment:

- Server status
- Current timestamp (UTC)
- Python version
- Operating system

This endpoint is useful for Docker, Kubernetes, and monitoring systems.

---

## 🧠 Why This Project?

This project follows common backend best practices:
- Separation of concerns
- Clear folder structure
- Testable and scalable design
- Production-ready foundation

It can be easily extended with:
- Database integration
- Authentication
- Dependency injection
- Docker & CI/CD pipelines

---

## 📄 License

MIT License
