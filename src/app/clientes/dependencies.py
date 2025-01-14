from core.session import get_db_connection
from fastapi import Depends
from safi.core import Connector
from .services import ClienteServices

def get_cliente_services(db:Connector = Depends(get_db_connection)):
    return ClienteServices(db)