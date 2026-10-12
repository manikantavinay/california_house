FROM python:3.11-slim

    WORKDIR /app

    COPY requirements.txt .

    COPY califianio.joblib .
    COPY . .

    RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

CMD ["python","app2.py"]
