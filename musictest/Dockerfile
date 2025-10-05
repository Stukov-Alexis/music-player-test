FROM python:3.11-slim

WORKDIR /app
COPY app/app.py ./app.py
RUN pip install flask
COPY templates ./templates
COPY static ./static

VOLUME ["/music"]

EXPOSE 5000
CMD ["python", "app.py"]
