"""Define each sqlalchemy model used for this project."""
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.types import Enum

from .enum import MindfulTextType, VideoType
from .plugins import db


class BaseModel(db.Model):
    """Base model. Subclass to include default fields defined below."""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @declared_attr.directive
    def __tablename__(cls):
        return cls.__name__.lower()


class Video(BaseModel):
    """Model storing links to mindful videos such as mediation and yoga."""
    url = db.Column(db.Text, nullable=False)
    type = db.Column(Enum(VideoType), nullable=False)
    duration_seconds = db.Column(db.Integer)

    def get_slack_msg(self):
        msg = f"Take a short break to follow along with this mindfulness video:\n\n{self.url}"
        if self.type == VideoType.AMBIANCE:
            msg = f"Enjoy this ambiance in the background while you work today:\n\n{self.url}"
        return msg
    

class MindfulText(BaseModel):
    """Model storing mindful text such as words of affirmation and mantras."""
    content = db.Column(db.Text, nullable=False)
    type = db.Column(Enum(MindfulTextType), nullable=False)
    is_quote = db.Column(db.Boolean, default=False)
    author = db.Column(db.String)

    def get_slack_msg(self):
        msg = self.content
        if self.type == MindfulTextType.MANTRA:
            msg = (
                "Take a few minutes, get into a comfortable position, close your eyes"
                " or settle your gaze, and repeat this phrase:\n\n"
            ) + msg
        elif self.type == MindfulTextType.REFLECTION:
            msg = "Take a few minutes to reflect. Here's a prompt to get you started:\n\n" + msg
        return msg
