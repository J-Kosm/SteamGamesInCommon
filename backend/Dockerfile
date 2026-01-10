FROM python:3.14

WORKDIR /app

RUN apt-get update && apt-get install -y iputils-ping

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]