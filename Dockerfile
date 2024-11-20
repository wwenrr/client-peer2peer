FROM python:latest
RUN apt-get update
WORKDIR /app
COPY . /app
RUN chmod +x run.sh
CMD ["./run.sh"]

