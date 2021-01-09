# base image
FROM python:3.8-slim

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /app

# add and install requirements
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY ./run_consumer.sh /app/run_consumer.sh
RUN chmod +x /app/run_consumer.sh

# add app
COPY . /app

# run server
CMD ["/app/entrypoint.sh"]
