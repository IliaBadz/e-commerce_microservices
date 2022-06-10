# PULL THE OFFICIAL BASE IMAGE
FROM python:3.9.6-slim-buster

# SET WORKING DIRECTORY
WORKDIR /usr/src/app

# SET ENNIRONMENT VARIABLES
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

# INSTALL SYSTEM DEPENDENCIES
RUN apt-get update \
	&& apt-get -y install netcat gcc \
	&& apt-get clean


ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv /opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# INSTALL PYTHON DEPENDENCIES
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# ADD APP
COPY . .

ENV PYTHONPATH=.