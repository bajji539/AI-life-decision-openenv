import random

from .models import Action


def set_seed(seed: int = 42) -> None:
    random.seed(seed)


def random_action() -> Action:
    return random.choice(list(Action))
