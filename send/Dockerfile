FROM python:alpine3.17

WORKDIR /usr/src/app

COPY ./src/* ./

COPY requiremets.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requiremets.txt

CMD ["python3", "send.py"]