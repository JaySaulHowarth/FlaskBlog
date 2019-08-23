FROM python:3.7
WORKDIR /application
RUN apt update
ENV FLASK_ENV production
ENV FLASK_APP run.py
COPY requirements .
RUN pip install -r requirements
COPY . .
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
