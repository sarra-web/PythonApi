FROM python:3.11-alpine
WORKDIR /app
COPY . /usr/app
COPY .env .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install python-dotenv
COPY api.py .
CMD ["python", "api.py"]