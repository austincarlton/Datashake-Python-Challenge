from fastapi import FastAPI
from app.routes import register_routes

app = FastAPI(title="Currency Converter API", version="1.0")

register_routes(app)
