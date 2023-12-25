FROM ubuntu

USER root
RUN mkdir project
RUN mkdir reports
WORKDIR project

COPY tests ./tests
COPY requirements.txt .

RUN apt-get update
RUN apt-get install wget gnupg ca-certificates -y
#add google repository
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && sh -c \
    'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

RUN apt-get update
RUN apt-get install apt-utils python3 python3-pip vim google-chrome-stable -y
RUN ln /usr/bin/python3 /usr/bin/python
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --upgrade -r requirements.txt