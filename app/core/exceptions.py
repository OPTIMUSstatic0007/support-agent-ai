from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logging import logger


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers.
    """

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        logger.exception(
            f"Unhandled exception on {request.method} {request.url.path}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "message": "Internal server error",
                },
            },
        )