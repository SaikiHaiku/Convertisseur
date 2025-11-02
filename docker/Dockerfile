FROM python:3.11-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
ffmpeg \
&& rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY converter /app/converter
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
