FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=development \
    PYTHONUNBUFFERED=1

EXPOSE 8600

CMD ["python", "run.py"]
