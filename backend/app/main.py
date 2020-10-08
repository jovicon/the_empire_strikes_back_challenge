import logging

from fastapi import FastAPI

from app.api import crews, ping
from app.db import init_db
from fastapi.middleware.cors import CORSMiddleware

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    application.include_router(ping.router)
    application.include_router(crews.router, prefix="/crews", tags=["crews"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
