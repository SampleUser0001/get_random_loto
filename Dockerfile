FROM python:3.9

USER root

WORKDIR /app
COPY app /app
COPY loto7.sh /

RUN chmod 755 /loto7.sh

CMD ["/loto7.sh"]
