FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_HOME=/usr/src/app

RUN apt-get update && \
        apt-get install -y postgresql-client-common

RUN mkdir -p $APP_HOME/static
RUN mkdir -p $APP_HOME/media

RUN groupadd -g 999 app && \
        useradd -r -u 999 -g app app

RUN chown -R app:app $APP_HOME

WORKDIR $APP_HOME

COPY ./sts/requirements.txt $APP_HOME
RUN pip install -r requirements.txt

USER 999

COPY ./sts/entrypoint.sh $APP_HOME

ENTRYPOINT ["./entrypoint.sh"]
EXPOSE 8081

COPY ./sts/ $APP_HOME

