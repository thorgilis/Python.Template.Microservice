# Python Microservice Template

A template for creating Python microservices with a complete linting and code quality setup.

## Features

- FastAPI framework for high performance
- Complete linting and code quality setup
- Docker and Docker Compose configuration
- GitHub Actions CI pipeline
- Structured logging
- Comprehensive test setup

## Code Quality Tools

- **Black**: Code formatter
- **isort**: Import sorter
- **flake8**: Style guide enforcement
- **mypy**: Static type checking
- **pylint**: Code analysis
- **bandit**: Security linter
- **pre-commit**: Git hooks manager

## Getting Started

### Prerequisites

- Python 3.12+
- Docker and Docker Compose (optional)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-microservice-template.git
   cd python-microservice-template
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
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

### Running the Application

#### Local Development

```bash
uvicorn app.main:app --reload
```

#### Using Docker

```bash
docker-compose up --build
```

### Running Tests

```bash
pytest
```

### Running Linters

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Or run individual tools
black .
isort .
flake8
mypy .
pylint app tests
```

## Project Structure

```
python-microservice-template/
├── app/                  # Application code
│   ├── api/              # API routes and models
│   ├── core/             # Core application components
│   └── services/         # Business logic
├── tests/                # Test files
├── .github/              # GitHub workflows
├── .gitignore            # Git ignore file
├── .pre-commit-config.yaml  # Pre-commit configuration
├── pyproject.toml        # Python project configuration
├── setup.py              # Package setup script
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
├── Dockerfile            # Docker configuration
└── docker-compose.yml    # Docker Compose configuration
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
