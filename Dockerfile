FROM python:3.9

USER root

WORKDIR /app
COPY app /app
COPY loto.sh /

RUN chmod 755 /loto.sh

CMD ["/loto.sh"]
