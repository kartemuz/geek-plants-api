from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title='Schedule'
    )

    return app
