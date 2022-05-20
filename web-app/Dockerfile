FROM ubuntu:18.04

RUN apt-get update -y 
RUN apt-get install -y python2.7
RUn apt-get install -y pip

RUN pip install flask 
RUN pip install flask-mysql

COPY . /opt/source-code 
ENTRYPOINT [ "FLASK_APP=/opt/source-code/app.py flask run" ]

  