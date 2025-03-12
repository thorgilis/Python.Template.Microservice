"""Setup Entry Point."""

from setuptools import find_packages, setup

setup(
    name="python-microservice",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.12",
    install_requires=[
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
        "pydantic>=2.6.0",
        "python-dotenv>=1.0.0",
    ],
)
