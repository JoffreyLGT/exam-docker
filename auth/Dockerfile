FROM python:latest
WORKDIR /usr/src/app
COPY ./auth.sh .
COPY ./auth.test.py . 
RUN pip install --no-cache-dir requests
ENTRYPOINT ["/bin/bash", "auth.sh"] 
