from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import rooms, autocomplete, ws
from app.db import models, session

models.Base.metadata.create_all(bind=session.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",    # Local development
        "https://twinco.netlify.app" # Production Netlify deployment
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(autocomplete.router, prefix="/autocomplete", tags=["autocomplete"])
app.include_router(ws.router, prefix="/ws", tags=["websocket"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Pair Programming App!"}
