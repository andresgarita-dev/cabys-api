from pydantic_settings import BaseSettings
import os


class Settings():
    app_name: str = os.getenv('APP_NAME', 'No se encontró la variable')


class DevelopmentConfig(Settings):
    app_env: str = 'development'


class TestingConfig(Settings):
    app_env: str = 'testing'


class StagingConfig(Settings):
    app_env: str = 'staging'


class ProductionConfig(Settings):
    app_env: str = 'production'


settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
