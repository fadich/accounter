FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/django
WORKDIR /opt/django
RUN pip install --upgrade pip
ADD requirements.txt /opt/django/
RUN pip install -r requirements.txt
ADD . /opt/django/
