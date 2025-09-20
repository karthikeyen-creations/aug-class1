from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
import os
import uvicorn

Agent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_SERVICE_URL = ["*", "http://localhost:8080"]

SERVE_WEB = True

app: FastAPI = get_fast_api_app(
    agents_dir=Agent_dir,
    allow_origins=ALLOWED_SERVICE_URL,
    web=SERVE_WEB,
)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
