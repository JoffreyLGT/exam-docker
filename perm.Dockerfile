FROM python:latest
WORKDIR /usr/src/app
ENV LOG=1
COPY ./perm.test.py . 
RUN pip install --no-cache-dir requests
ENTRYPOINT ["python", "perm.test.py"]
