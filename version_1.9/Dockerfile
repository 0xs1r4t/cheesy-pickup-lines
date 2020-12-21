FROM python:3.8.5
WORKDIR /app

COPY .env .
COPY main.py .
COPY requirements.txt .
COPY text_files/* .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]