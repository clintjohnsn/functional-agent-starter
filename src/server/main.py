"""Set up the FastAPI application."""

import logging
import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path

import ell
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.config.settings import settings
from server.routes.api.v1 import api

config = settings()
logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# FastAPI lifespan manager - Startup and Shutdown Events
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Handle FastAPI startup and shutdown events."""
    # Startup events
    ell.init(store="./.logdir", autocommit=True, verbose=True) # Initialize ell prompt logging
    logger.info("Started FastAPI application")
    yield # Yield control to the FastAPI application
    # Shutdown events
    logger.info("Shutting down FastAPI application") 

# Initialize the FastAPI application
app = FastAPI(
    lifespan=lifespan,
    title=config.PROJECT_NAME,
    description=config.PROJECT_DESCRIPTION,
    version=config.VERSION
)

# CORS
app.add_middleware(
    CORSMiddleware,
    **config.cors_config,
)

# Register the API routes
app.include_router(api.router)
