import os
import modal
import sys
docker_image = os.environ.get(
    "DOCKER_IMAGE_TAG",
    "devchuz/mlops-fastapi-microservice:latest",
)

modal_app_name = os.environ.get(
    "MODAL_APP_NAME",
    "mlops-fastapi-qas",
)

image = modal.Image.from_registry(
    docker_image
)

app = modal.App(modal_app_name)


@app.function(image=image)
@modal.asgi_app()
def fastapi_app():
    sys.path.insert(0, "/app")

    from src.core.server import app as web_app

    return web_app