FROM python:latest
RUN pip install websockets
EXPOSE 8001
WORKDIR /usr/src/app
COPY test_client.py .
CMD ["python3", "test_client.py"]
