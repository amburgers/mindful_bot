from flask import Blueprint

from .plugins import db
from .models import MindfulText, Video
from .seed_data.mindful_text import mindful_text_seed_data
from .seed_data.video import video_seed_data


seed_data_bp = Blueprint('seed_data', __name__)


@seed_data_bp.cli.command("text")
def seed_text():
    """Seeds MindfulText data."""
    print("Seeding MindfulText data")
    count = 0
    for obj in mindful_text_seed_data:
        mindful_text = MindfulText(
            content=obj["content"],
            type=obj["type"],
            is_quote=obj.get("is_quote"),
            author=obj.get("author"),
        )
        db.session.add(mindful_text)
        count += 1
    db.session.commit()
    print(f"{count} MindfulTexts created")


def duration_str_to_seconds(string_time):
    time_list = string_time.split(":")
    if len(time_list) == 2:
        time_list = ["0"] + time_list
    hours, minutes, seconds = time_list
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


@seed_data_bp.cli.command("video")
def seed_video():
    """Seeds Video data."""
    print("Seeding Video data")
    count = 0
    for obj in video_seed_data:
        duration = obj["duration"]
        duration_seconds = duration_str_to_seconds(duration)
        video = Video(
            url=obj["url"],
            type=obj["type"],
            duration_seconds=duration_seconds,
        )
        db.session.add(video)
        count += 1
    db.session.commit()
    print(f"{count} Videos created")