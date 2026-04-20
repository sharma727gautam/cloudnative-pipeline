import os


class Config:
    APP_NAME = os.environ.get("APP_NAME", "cloudnative-pipeline")
    VERSION = os.environ.get("APP_VERSION", "1.0.0")
    PORT = int(os.environ.get("PORT", 5000))


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "production"


config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
