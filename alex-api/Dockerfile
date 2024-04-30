FROM python:3.11

WORKDIR /app/api 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python api/manage.py makemigrations 
RUN python api/manage.py migrate

CMD ["python", "api/manage.py", "runserver", "0.0.0.0:8000"]

