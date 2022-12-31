# base image  
FROM python:3.11.1-slim   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY requirements.txt $DockerHOME
  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  

COPY . $DockerHOME
COPY db.sqlite3 $DockerHOME

RUN python manage.py makemigrations && python manage.py migrate

# port where the Django app runs  
EXPOSE 8000  

# start server  
CMD python manage.py runserver  