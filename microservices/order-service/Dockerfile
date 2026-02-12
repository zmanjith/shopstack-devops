FROM python:3.10-slim
WORKDIR /app
COPY app/ .
RUN pip install flask requests
EXPOSE 5002
CMD ["python", "app.py"]

