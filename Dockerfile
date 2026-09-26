FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run sets PORT (defaults to 8080). Bind gunicorn to it.
ENV PORT=8080
EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 --timeout 60 app:app
