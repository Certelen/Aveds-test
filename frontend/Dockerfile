FROM python:3.11-slim

WORKDIR /app

COPY ./frontend ./

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["python", "main.py"]  