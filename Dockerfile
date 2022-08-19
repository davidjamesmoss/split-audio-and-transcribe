FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    python3-software-properties \
    python3.6 \
    python3-pip \
    python3-dev \
    ffmpeg

VOLUME /src

RUN pip3 install pydub speechrecognition
ENTRYPOINT ["python3", "/src/splitter.py"]
