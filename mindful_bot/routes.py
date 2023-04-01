"""This module defines the routes available to the flask app."""
import random

from flask import Blueprint, request, make_response
from slack_sdk import WebClient
from sqlalchemy.sql.expression import func

from .config import SLACK_BOT_TOKEN
from .models import MindfulText, Video


requestbp = Blueprint("request_blueprint", __name__)
slack_client = WebClient(SLACK_BOT_TOKEN)


@requestbp.route("/")
def hello():
    return 'Hello, today is a great day to be mindful!'


@requestbp.route("/mindful", methods=["POST"])
def mindful():
    info = request.form
    channel = info["channel_id"]
    filter = info.get("text")
    if filter == "text":
        model = MindfulText
    elif filter == "video":
        model = Video
    else:
        model = random.choice([Video, MindfulText])

    # Query for random object and format its slack message
    obj = model.query.order_by(func.random()).limit(1).first()
    message = obj.get_slack_msg()
    blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": message
			}
		}
	]

    slack_client.chat_postMessage(
        channel= channel,
        text="Take time for some mindful minutes",
        blocks=blocks,
    )
    return make_response("", 200)
