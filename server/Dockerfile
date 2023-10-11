FROM python:3.11

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

RUN pip install fastapi
RUN pip install uvicorn[standard]
RUN pip install gunicorn
