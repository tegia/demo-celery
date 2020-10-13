FROM ubuntu:20.04


RUN apt-get update -qq

RUN apt-get install locales && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip build-essential python3-dev \
    libmysqlclient-dev libxml2-dev libxslt1-dev libssl-dev libffi-dev

ENV C_FORCE_ROOT true

ENV DEBUG true
# copy source code
COPY . /celery_transaction_mongo
WORKDIR /celery_transaction_mongo

# install requirements
RUN pip3 install -r requirements.txt
# run the app server
# ENTRYPOINT ["python3"]
# CMD ["app.py"]
ENTRYPOINT honcho -f Procfile start
