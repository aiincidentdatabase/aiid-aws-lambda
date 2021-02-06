# Container image that runs your code
FROM public.ecr.aws/lambda/python:3.8

RUN apt-get update && \
    apt-get -y install curl make gcc python-dev libffi-dev musl-dev libxml2-dev libxslt-dev openssl-dev zlib-dev jpeg-dev

RUN pip install --upgrade pip && \
    pip install --no-cache-dir news-please

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
