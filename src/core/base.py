
from safi.core import Connector


class BaseServices():
    def __init__(self, db: Connector):
        self.db = db

    def signup(self, user: SAFISessionToken, app_name: str = 'API REST'):
        session_data = user.model_dump()
        session_data["app_name"] = app_name
        self.db.impersonate(**session_data)

