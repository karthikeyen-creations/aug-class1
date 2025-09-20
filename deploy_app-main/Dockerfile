FROM python:3.13-slim
WORKDIR /app

COPY requirement.txt .
RUN pip install -r requirement.txt

COPY . .
EXPOSE 8080

ENTRYPOINT ["uvicorn"]
CMD ["finalapp:app","--host","0.0.0.0","--port","8080"]
