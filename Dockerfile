FROM python:3.9
WORKDIR /app
RUN pip3 install pandas boto3 requests
COPY . .
CMD ["python", "./tickets_in.py"]
