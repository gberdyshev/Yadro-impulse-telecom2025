FROM ubuntu:22.04

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y python3 python3-pip

COPY script.py req.txt .

RUN pip3 install -r req.txt

CMD ["python3", "./script.py"]