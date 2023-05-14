FROM python:latest
WORKDIR /usr/src/app
ENV LOG=1
COPY ./sentiment.test.py . 
RUN pip install --no-cache-dir requests
ENTRYPOINT ["python", "sentiment.test.py"]
