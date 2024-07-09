from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    app_name: str = os.getenv('APP_NAME', 'No se encontró la variable')


class DevelopmentConfig(BaseSettings):
    app_env: str = 'development'
    pass


class TestingConfig(BaseSettings):
    app_env: str = 'testing'
    pass


class StagingConfig(BaseSettings):
    app_env: str = 'staging'
    pass


class ProductionConfig(BaseSettings):
    app_env: str = 'production'
    pass


settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
