"""
Main FastAPI Caller
"""
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import crews, ping
from app.db import init_db

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    """
    Create aplication definition

    * cors protection and access configured
    """
    application = FastAPI()
    origins = [
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
    """
    startup event definition
    """
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    """
    shutdown event definition
    """
    log.info("Shutting down...")
