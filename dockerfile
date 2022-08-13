FROM python:3.8-alpine
ENV PATH="/scripts:${PATH}"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt 
RUN apk add --no-cache postgresql-libs jpeg-dev zlib-dev gcc 
RUN apk add --update --no-cache --virtual .tmp postgresql-dev musl-dev libc-dev linux-headers python3-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./JobOffersSite /app
WORKDIR /app
EXPOSE 8000
COPY ./scripts /scripts

RUN chmod +x /scripts/*
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
