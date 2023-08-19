FROM ubuntu:latest
LABEL authors="Antonio"

ENTRYPOINT ["top", "-b"]