FROM python:latest
WORKDIR /usr/src/app
COPY ./perm.test.py . 
COPY ./perm.sh .
RUN pip install --no-cache-dir requests
ENTRYPOINT ["/bin/bash", "perm.sh"]
