FROM python:3.10
ENV TZ=Asia/Taipei
WORKDIR /django
COPY . .

RUN apt-get update && apt-get -y install cron && apt-get -y install redis-server && \ 
    apt-get install nano && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN touch /var/log/django.log && chmod 666 /var/log/django.log
RUN chmod 711 /django/manage.py

CMD python ./manage.py runserver 0.0.0.0:8000