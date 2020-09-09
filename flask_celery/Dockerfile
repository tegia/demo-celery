FROM ubuntu:20.04


RUN apt-get update -qq

RUN apt-get install locales && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip build-essential python3-dev \
    libmysqlclient-dev libxml2-dev libxslt1-dev libssl-dev libffi-dev

ENV C_FORCE_ROOT true


# copy source code
COPY . /flask_celery
WORKDIR /flask_celery

# install requirements
RUN pip3 install -r requirements.txt


# run the worker
#ENTRYPOINT ['celery']
#CMD ['-A','tasks', 'worker','--loglevel=info']
ENTRYPOINT honcho -f Procfile start