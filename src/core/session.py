from safi.core import Connector
from .settings import get_db_settings

def get_db_connection():
    db=Connector(**get_db_settings())
    return db
    