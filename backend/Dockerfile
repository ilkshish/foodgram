FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "foodgram_backend.wsgi:application", "--bind", "0.0.0.0:8000"]