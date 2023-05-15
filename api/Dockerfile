FROM datascientest/fastapi:1.0.0
RUN apt -y update && apt -y install curl
HEALTHCHECK --interval=5s --timeout=3s \
    CMD curl -f http://0.0.0.0:8000/status || exit 1
