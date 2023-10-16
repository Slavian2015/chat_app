FROM python:3.11

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

RUN pip install fastapi
RUN pip install uvicorn[standard]
RUN pip install gunicorn
RUN pip install openai
RUN pip install llm-client
RUN pip install llama-index

RUN pip install typing_extensions
RUN pip install types-requests
RUN pip install dependency-injector
RUN pip install Faker
RUN pip install flake8
RUN pip install pydantic
RUN pip install pytest
RUN pip install pytest-mock
RUN pip install mypy
RUN pip install mypy-extensions
RUN pip install urllib3
RUN pip install starlette
RUN pip install validators
RUN pip install websockets
RUN pip install Werkzeug
RUN pip install pydantic-settings
RUN pip install httpx