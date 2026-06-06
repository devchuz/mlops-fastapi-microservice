# src/api/v1/routes.py

from fastapi import APIRouter, Depends, status
from fastapi.responses import PlainTextResponse

from src.app.services.model_service import PredictionInput, PredictionService

router = APIRouter()


GITHUB_ASCII_ART = r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              GitHub Community Day Perú                       ║
║                                                              ║
║        Developer Student Clubs - UTP                         ║
║        Universidad Tecnológica del Perú                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   ____ _ _   _   _       _                                   ║
║  / ___(_) |_| | | |_   _| |__                                ║
║ | |  _| | __| |_| | | | | '_ \                               ║
║ | |_| | | |_|  _  | |_| | |_) |                              ║
║  \____|_|\__|_| |_|\__,_|_.__/                               ║
║                                                              ║
║              /\_/\                                           ║
║             ( o.o )        Octocat says:                     ║
║              > ^ <         Build. Ship. Deploy.              ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   Demo: AI Model Deployment Pipeline                         ║
║                                                              ║
║   1. Code pushed to GitHub                                   ║
║   2. GitHub Actions runs tests                               ║
║   3. Docker image is built                                   ║
║   4. Docker image is pushed to registry                      ║
║   5. FastAPI model service is deployed on Modal              ║
║                                                              ║
║   Stack: FastAPI + Docker + GitHub Actions + Modal           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {
        "status": "healthy",
        "message": "API is running correctly"
    }


@router.get("/github", status_code=status.HTTP_200_OK)
async def github_event():
    return {
        "event": "GitHub Community Day Perú",
        "message": "Welcome to the MLOps FastAPI deployment demo",
        "topic": "AI model deployment pipeline with GitHub Actions, Docker and Modal",
        "community": "Developer Student Clubs UTP",
        "platform": "GitHub"
    }


@router.get("/github-ascii", response_class=PlainTextResponse)
async def github_ascii():
    return GITHUB_ASCII_ART


@router.post("/predict")
async def predict(
    input_data: PredictionInput,
    service: PredictionService = Depends()
):
    prediction = service.predict(input_data)

    return {
        "prediction": prediction.tolist(),
        "demo": "GitHub Community Day Perú",
        "pipeline": "FastAPI + Docker + GitHub Actions + Modal"
    }