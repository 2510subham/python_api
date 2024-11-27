FROM python:3.14.0a2-slim-bullseye

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py

CMD ["python", "-m uvicorn", "main:app","--reload", "--port", "80"]