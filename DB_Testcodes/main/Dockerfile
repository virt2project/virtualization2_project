FROM python:latest
RUN pip3 install numpy pandas
WORKDIR /run
COPY main.py .
ENTRYPOINT ["python3", "main.py"]
