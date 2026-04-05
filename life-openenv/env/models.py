from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    WORK = "WORK"
    STUDY = "STUDY"
    REST = "REST"
    SOCIALIZE = "SOCIALIZE"

    def __str__(self):
        return self.value


@dataclass
class LifeState:
    energy: int = 80
    stress: int = 20
    money: int = 500
    happiness: int = 50
    skill_level: int = 10
    day: int = 0

    def to_dict(self):
        return {
            "energy": self.energy,
            "stress": self.stress,
            "money": self.money,
            "happiness": self.happiness,
            "skill_level": self.skill_level,
            "day": self.day,
        }
