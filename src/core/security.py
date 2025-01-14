from fastapi import Depends
from pydantic import BaseModel, ConfigDict,typing,Field
from datetime import datetime
from core.settings import get_security_params

import jwt




## ToKen
class BaseToken(BaseModel):
    exp: datetime

class SAFISessionToken(BaseToken):
    model_config = ConfigDict(populate_by_name=True)
    Usuario:int =  Field(...,alias="user_id")
    Sucursal:int =Field(...,alias="branch_id")
    DireccionIP:str=Field(...,alias="host")


class Security():

    def decode(token: str) :
        security=get_security_params()
        secret_key=security.get("secret_key","")
        algorithm=security.get("encrypt_algorithm","")
        try:
            token_data = jwt.decode(token, secret_key, algorithms=[algorithm])
            print(token_data)
            return SAFISessionToken(**token_data)
        except jwt.PyJWTError as e:
            print(e)
            return None


