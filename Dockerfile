FROM python:3.9-alpine

WORKDIR /crawler

COPY crontab /etc/cron.d/crontab

COPY . /crawler

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

RUN crontab /etc/cron.d/crontab

RUN touch /tmp/out.log

CMD crond && tail -f /tmp/out.log