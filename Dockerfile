# Container image that runs your code
FROM public.ecr.aws/lambda/python:3.8

RUN yum -y groupinstall "Development tools"
RUN yum -y install gcc-c++ libcurl-devel cmake3 git

RUN pip install --upgrade pip && \
    pip install --no-cache-dir news-please cchardet

COPY parsenews.py /var/task/

CMD ["parsenews.lambda_handler"]
