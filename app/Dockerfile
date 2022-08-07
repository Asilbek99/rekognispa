FROM python:3
ENV PYTHONUNBUFFERED=1
ARG PROJECT_PATH
ARG SECRET_KEY
ARG S3_BUCKET_NAME
ARG S3_BUCKET_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

WORKDIR /application
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python manage.py flush --no-input
RUN python manage.py migrate --no-input --run-syncdb
RUN python manage.py collectstatic --no-input
EXPOSE 8000