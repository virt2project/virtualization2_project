FROM python:latest
RUN pip install websockets
EXPOSE 8001
WORKDIR /usr/src/app
COPY test_serv.py .
CMD ["python3", "test_serv.py"]
