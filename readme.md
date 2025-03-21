# Python Microservice Template

A production-ready template for building FastAPI microservices with best practices in code quality, security, and deployment.

## 🚀 Features

- **FastAPI** – High-performance Python web framework
- **Code Quality & Linting** – Pre-configured tools for clean, maintainable code
- **Docker & Docker Compose** – Easy containerization and deployment
- **GitHub Actions CI** – Automated testing and linting
- **Structured Logging** – Better observability
- **Comprehensive Testing** – Preconfigured pytest setup

## 🛠 Code Quality Tools

- **Black** – Code formatter
- **isort** – Import sorter
- **flake8** – Style guide enforcement
- **mypy** – Static type checking
- **pylint** – Code analysis
- **bandit** – Security linter
- **pre-commit** – Automate checks before committing

## ⚡ Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose (optional)

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/thorgilis/Python.Template.Microservice.git
   cd Python.Template.Microservice
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```
5. Setup configuration:
   ```bash
   cp .env.template .env
   # Edit values as needed
   ```

## ▶ Running the Application

### Local Development
```bash
uvicorn app.main:app --reload
```

### Using Docker
```bash
docker-compose up --build
```

## 🧪 Running Tests
```bash
pytest --cov=app tests/ --cov-report=xml
```

## 🔍 Running Linters
```bash
pre-commit run --all-files
```

## 📂 Project Structure

```
Python.Template.Microservice/
├── app/                     # Application code
│   ├── api/                 # API routes and models
│   ├── core/                # Core application components
│   └── services/            # Business logic
├── tests/                   # Test files
├── .github/
│   └── workflows/
│     └── ci.yml             # CI workflow configuration
├── .flake8                  # Linter configuration
├── .gitignore               # Git ignore file
├── .pre-commit-config.yaml  # Pre-commit configuration
├── bandit.yaml              # Bandit configuration
├── pyproject.toml           # Python project configuration
├── setup.py                 # Package setup script
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── Dockerfile               # Docker configuration
└── docker-compose.yml       # Docker Compose configuration
```

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.
