from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name:str = "FastAPI K8s Microservices Starter"

    class Config:
        env_file= ".env"

settings= Settings()
