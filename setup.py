# File setup.py

from setuptools import setup, find_packages

setup(
    name="fastapi_auth_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.109.0",
        "uvicorn==0.27.0",
        "pydantic==2.5.3",
        "pydantic-settings==2.1.0",
    ],
)