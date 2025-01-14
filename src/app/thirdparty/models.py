from decimal import Decimal
from pydantic import BaseModel, Field

class CheckClientDataRequest(BaseModel):
    client_id:int=Field(description="Client ID",example=1)
    device_id:str=Field(description="Device ID",example=1)
    user_id:str=Field(description="User ID",example=1)
    key:str=Field(description="Field ID",example=1)
    value:str=Field(description="Value",example=1.0)
    
    