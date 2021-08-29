ARG PROJECT_PATH=

FROM python:3
ENV PYTHONUNBUFFERED=1
ARG PROJECT_PATH
WORKDIR ${PROJECT_PATH}
COPY requirements.txt ${PROJECT_PATH}
RUN pip install -r requirements.txt
COPY . ${PROJECT_PATH}
RUN python manage.py flush --no-input
RUN python manage.py migrate --no-input --run-syncdb
RUN python manage.py collectstatic --no-input
EXPOSE 8000