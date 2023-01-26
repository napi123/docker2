FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/* .
ENV FLASK_APP="myapp"
ENV FLASK_DEBUG=1
ENV FLASK_RUN_HOST="0.0.0.0"
CMD ["flask", "run"]