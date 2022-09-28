FROM python:3.10

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt &&\
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media



