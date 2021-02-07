# Container image that runs your code
FROM public.ecr.aws/lambda/python:3.8

RUN yum -y groupinstall "Development tools"
RUN yum -y install gcc-c++ libcurl-devel cmake3 git

RUN pip install --upgrade pip && \
    pip install --no-cache-dir news-please cchardet

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY parsenews.py /var/task/

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/var/task/parsenews.py"]
