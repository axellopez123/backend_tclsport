from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.routes.product import router as product_router
from app.auth.routes.auth import router as auth_router

from typing import List

import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

origins = [
    "https://inmobiliaria.arwax.pro",
    "http://localhost:5173",   # Tu frontend local
    "https://back-properties.arwax.pro",  
]

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()
    await init_db()

app.include_router(auth_router, prefix="/api")


# # Crear el directorio media si no existe
# os.makedirs("media", exist_ok=True)

# # Montar la carpeta media en /media
# app.mount("/media", StaticFiles(directory="media"), name="media")
