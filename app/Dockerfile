ARG PROJECT_PATH=/usr/share/webapps/rekognispa
FROM python:3.9
ENV PYTHONUNBUFFERED=1
ARG PROJECT_PATH
ARG SECRET_KEY
ARG S3_BUCKET_NAME
ARG S3_BUCKET_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
WORKDIR ${PROJECT_PATH}
COPY requirements.txt ${PROJECT_PATH}
RUN pip install -r requirements.txt
COPY . ${PROJECT_PATH}
RUN python manage.py flush --no-input
RUN python manage.py migrate --no-input --run-syncdb
RUN python manage.py collectstatic --no-input
EXPOSE 8000