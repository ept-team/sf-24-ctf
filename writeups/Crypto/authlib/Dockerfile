FROM python:3.11-slim-bookworm 
COPY . /app

RUN python3 -m pip install -r /app/requirements.txt
WORKDIR /app
ENTRYPOINT ["python3", "main.py"]