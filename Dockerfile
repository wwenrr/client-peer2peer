FROM python:3.9-slim
RUN apt-get update
WORKDIR /app
COPY . /app
RUN chmod +x build.sh
RUN ./build.sh
ENTRYPOINT ["bash", "-c", "source lib/bin/activate && exec python3 -B -m src.run --reload"]

