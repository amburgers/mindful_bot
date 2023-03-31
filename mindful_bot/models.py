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


class MindfulText(BaseModel):
    """Model storing mindful text such as words of affirmation and mantras."""
    content = db.Column(db.Text, nullable=False)
    type = db.Column(Enum(MindfulTextType), nullable=False)
    is_quote = db.Column(db.Boolean, default=False)
    author = db.Column(db.String)
