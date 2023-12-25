FROM jenkins/jenkins:lts

COPY install_allure.py /home/install_allure.py

USER root

RUN apt-get update -y
RUN apt-get install wget python3 python3-pip vim -y
RUN ln /usr/bin/python3 /usr/bin/python
RUN python -m pip install --upgrade pip setuptools wheel requests

RUN python /home/install_allure.py

USER jenkins