ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8
RUN apk add --no-cache python3 py3-pip

# Copy data for add-on
COPY run.sh /
COPY requirements.txt /
COPY main.py /

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]