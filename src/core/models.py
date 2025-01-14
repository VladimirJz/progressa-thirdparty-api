from datetime import date, datetime
from typing import Optional

from decimal import Decimal
from pydantic import BaseModel, Field, HttpUrl


class ResponseMetaData(BaseModel):
    code:int=0
    http_code:int=500
    message:Optional[str]=None
    reference:Optional[str]=None
    sucess:bool=True
    diagnostic:Optional[str]=None

class _APIRespose(BaseModel):
    meta:ResponseMetaData
    
class TransactionResponse(_APIRespose):
    transaction:int=0
    status:str="PROCESADO"
    date_time:str
    amount:Decimal=0.0
    balance:Decimal=0
    due_balance:Decimal=0
    #receipt:Receipt
    model_config = {
 
        'fields': {
            'meta': {'exclude': {'diagnostic', 'reference', 'message'}}
        }
    }
   
    
class MessageResponse(_APIRespose):
    pass

class ErrorResponse(_APIRespose):
    pass
    
