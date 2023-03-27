from fastapi.exception_handlers import request_validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from app.exceptions.exception import AuthenticationError, ForbiddenError, InvalidTokenError, InvalidCredentialsError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import Request


def register(app):
    @app.exception_handler(AuthenticationError)
    async def authentication_exception_handler(request: Request, e: AuthenticationError):
        """
        认证异常处理
        """
        return JSONResponse(status_code=401, content={
            "error": e,
            "errorMessage": e.message
        })

    @app.exception_handler(ForbiddenError)
    async def authorization_exception_handler(request: Request, e: ForbiddenError):
        """
        权限异常处理
        """
        return JSONResponse(status_code=403, content={
            "error": 'ForbiddenOperationException',
            "errorMessage": e.message
        })

    @app.exception_handler(InvalidTokenError)
    async def exist_exception_handler(request: Request, e: InvalidTokenError):
        """
        重复异常处理
        """
        return JSONResponse(status_code=403, content={
            "error": 'ForbiddenOperationException',
            "errorMessage": e.message
        })

    @app.exception_handler(InvalidCredentialsError)
    async def exist_exception_handler(request: Request, e: InvalidCredentialsError):
        """
        重复异常处理
        """
        return JSONResponse(status_code=403, content={
            "error": 'ForbiddenOperationException',
            "errorMessage": e.message
        })

    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request: Request, exc):
        return await http_exception_handler(request, exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc):
        return await request_validation_exception_handler(request, exc)
