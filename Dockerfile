FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install redis
CMD ["python", "app.py"]

