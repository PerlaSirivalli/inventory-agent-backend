from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base

from routes.auth_routes import router as auth_router
from routes.product_routes import router as product_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(product_router)

# Create database tables
Base.metadata.create_all(bind=engine)

# Home route
@app.get("/")
def home():
    return {
        "message": "Inventory Agent Backend"
    }