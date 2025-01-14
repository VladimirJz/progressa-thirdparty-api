
from fastapi import Depends, HTTPException,status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from core.security import Security


security = HTTPBearer()
def validate_token(user_credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not user_credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se han proporcionado credenciales validas.",
        )
    
    if user_credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El esquema de autorización no esta permitido.",
        )

    token = user_credentials.credentials
    token_data=Security.decode(token)
    print(token_data)
    # Aquí podrías verificar el token (por ejemplo, usando JWT o una base de datos)
    #your_expected_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2MjEsImJyYW5jaF9pZCI6MSwiaG9zdCI6IjEwLjYuMzUuMTIiLCJleHAiOjE3MzE3OTc4NTd9.tJUmLzMVSzMjaOF-JzEIXM07uvYd7YVJkfsHbwut77Y"
    if not token_data :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El token no es valido o a expirado.",
        )
    return token_data