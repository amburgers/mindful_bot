import logging
from logging.config import dictConfig as load_dict_config

# from .adapters import SlackAdapter
from .config import LOGGING_CONFIG, SLACK_BOT_TOKEN

# Logging
load_dict_config(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Integrations
# slack = SlackAdapter(SLACK_BOT_TOKEN)

# Flask app
from .app import create_app  # noqa
from .models import *  # noqa