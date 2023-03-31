"""Define enums to be used throughout this project."""
import enum


class VideoType(enum.IntEnum):
    MEDITATION = 1
    YOGA = 2
    AMBIANCE = 3


class MindfulTextType(enum.IntEnum):
    AFFIRMATION = 1
    ADVICE = 2
    REFLECTION = 3
    MANTRA = 5
