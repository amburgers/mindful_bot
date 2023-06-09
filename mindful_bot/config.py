import os

BASE_URL = os.getenv("BASE_URL", "")
SECRET_KEY = os.getenv("SECRET_KEY", "shh-its-a-secret")

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///mindful_bot.db")

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", None)
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET", "TestSigningSecretSlack")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s %(name)s:%(lineno)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s %(message)s",  # noqa
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "standard", "level": "DEBUG"}
    },
    "loggers": {
        "": {"handlers": ["console"]}
    }
}
