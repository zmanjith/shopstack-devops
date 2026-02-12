FROM python:3.10-slim
WORKDIR /app
COPY app/ .
RUN pip install flask
EXPOSE 5003
CMD ["python", "app.py"]
