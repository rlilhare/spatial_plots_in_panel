# syntax=docker/dockerfile:1
# FROM python:latest
FROM ubuntu:xenial-20210429

COPY . /spatial_plotting
WORKDIR /spatial_plotting
RUN apt-get update -y
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update -y
RUN apt-get -y install python3.8 python3-pip
RUN apt-get -y install libgeos-c1v5 libgeos-dev python-dev python3-mpltoolkits.basemap python3-matplotlib
RUN pip install --upgrade pip
RUN pip3.8 install -r requirements.txt 
RUN pip3.8 install -r requirements_dev.txt
RUN python3.8 -m pip install --user https://github.com/matplotlib/basemap/archive/master.zip
CMD [ "python3", "main.py" ]