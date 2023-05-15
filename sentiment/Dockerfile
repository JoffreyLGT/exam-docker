FROM python:latest
WORKDIR /usr/src/app
COPY ./sentiment.test.py .
COPY ./sentiment.sh .
RUN pip install --no-cache-dir requests
ENTRYPOINT ["/bin/bash", "sentiment.sh"]
