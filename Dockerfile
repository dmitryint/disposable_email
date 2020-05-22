FROM python:3-alpine

COPY ./ /app
WORKDIR /app

RUN apk -U add build-base linux-headers pcre-dev pcre \
    && pip3 install 'uWSGI==2.0.17.1' \
    && pip3 install -r requirements.txt \
    && apk del build-base linux-headers pcre-dev

EXPOSE 5000
CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "--enable-threads", "--mount", "/=app:app"]
