from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    appkey: str
    appsecret: str
    CANO: str
    ACNT_PRDT_CD: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
settings = Settings()
