from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzQ3MzIwMTk4LCJpYXQiOjE3NDY3MTUzOTgsInN1YiI6IjIifQ.LvsIwd_FlfuUDBlXoUkBdZN1ooIMt4tuzvAFtO2MU4c
Tipo: bearer

Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzQ3MzIxNzU4LCJpYXQiOjE3NDY3MTY5NTgsInN1YiI6IjMifQ.qxgb8Y1nYE4eMiM2Dz1XJq9AiVR-ePlMeFAWqptBoY0
Tipo: bearer
"""