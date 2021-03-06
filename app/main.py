import uvicorn
from fastapi import FastAPI

from common.config import conf

# from app.common.config import conf


def create_app():
    c = conf()
    app = FastAPI()
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
