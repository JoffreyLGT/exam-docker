FROM python:latest
WORKDIR /usr/src/app
#ENV LOG=1
COPY ./perm.test.py . 
COPY ./perm.sh .
RUN pip install --no-cache-dir requests
ENTRYPOINT ["/bin/bash", "perm.sh"]
