FROM python:3.8-alpine
ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt requirements.txt 
RUN apk add --no-cache postgresql-libs jpeg-dev zlib-dev gcc musl-dev
RUN apk add --update --no-cache --virtual .tmp postgresql-dev libc-dev linux-headers python3-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./JobOffersSite /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
