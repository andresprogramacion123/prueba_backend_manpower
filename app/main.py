from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.utils.exceptions import AppExceptionCase

app = FastAPI()

# Controlador de excepciones
async def app_exception_handler(
    request: Request
    ,exc: AppExceptionCase
    ):
    return JSONResponse(
        status_code=exc.status_code
        ,content={"app_exception": exc.exception_case,"context": exc.context}
        )

@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)

@app.get("/")
def read_root():
    return {"Hola": "Mundito"}