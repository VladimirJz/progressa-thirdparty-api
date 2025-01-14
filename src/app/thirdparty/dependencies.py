from core.session import get_db_connection
from fastapi import Depends
from safi.core import Connector
from .services import  ThirdpartyServices

def get_service(db:Connector = Depends(get_db_connection)):
    return ThirdpartyServices(db)