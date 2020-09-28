FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install requests

COPY ./app /app/app
WORKDIR /app/app