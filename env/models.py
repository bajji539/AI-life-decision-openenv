from enum import Enum
from pydantic import BaseModel, Field


class Action(Enum):
    WORK = "WORK"
    STUDY = "STUDY"
    REST = "REST"
    SOCIALIZE = "SOCIALIZE"

    def __str__(self):
        return self.value


class LifeState(BaseModel):
    energy: int = Field(default=80, ge=0, le=100, description="Energy level (0-100)")
    stress: int = Field(default=20, ge=0, le=100, description="Stress level (0-100)")
    money: int = Field(default=500, ge=0, description="Money accumulated")
    happiness: int = Field(default=50, ge=0, le=100, description="Happiness level (0-100)")
    skill_level: int = Field(default=10, ge=0, description="Skill level (unbounded)")
    day: int = Field(default=0, ge=0, description="Current day")

    def to_dict(self):
        return self.model_dump()
