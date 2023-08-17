FROM python:3.10-slim-buster
WORKDIR /opt/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /opt/app
RUN python manage.py migrate
RUN python manage.py loaddata demo-data --format JSON
RUN python manage.py initadmin
CMD [ "python", "./manage.py", "runserver"]
