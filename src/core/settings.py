from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class AppSettings(BaseSettings):
    program_name:str='safi.core.engine'
    dbhost:str
    dbport:int
    dbuser:str
    dbpassword:str
    dbcore:str
    dbaddons:str
    encrypt_algorithm:str
    secret_key:str
    
    model_config = SettingsConfigDict(env_file='.env')


@lru_cache
def get_db_settings()->dict:
    print (AppSettings().model_dump(exclude={"encrypt_algorithm", "secret_key"}))
    db_settings=AppSettings().model_dump(exclude={"encrypt_algorithm", "secret_key"})
    
    return db_settings

@lru_cache
def get_security_params()->dict:
    security_params =  AppSettings().model_dump(include={"encrypt_algorithm", "secret_key"})
    print(type(security_params))
    return security_params
