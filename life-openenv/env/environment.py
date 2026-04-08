import random
from dataclasses import asdict

from .models import Action, LifeState


class LifeEnvironment:
    def __init__(self, seed: int = 42):
        self.seed = seed
        random.seed(self.seed)
        self.state = LifeState()
        self.max_days = 100

    def reset(self) -> LifeState:
        random.seed(self.seed)
        self.state = LifeState()
        return self.state

    def get_state(self) -> LifeState:
        """Return the current state (OpenEnv compliance)."""
        return self.state

    def get_observation(self) -> dict:
        return self.state.to_dict()

    def step(self, action: Action) -> tuple[dict, float, bool]:
        if not isinstance(action, Action):
            raise ValueError("Invalid action provided to environment")

        self._apply_action(action)
        self._natural_decay()
        self._apply_random_event()
        self._clamp_state()
        reward = self._calculate_reward()
        self.state.day += 1
        done = self.state.day >= self.max_days or self.state.energy <= 0
        return self.get_observation(), reward, done

    def _apply_action(self, action: Action) -> None:
        if action == Action.WORK:
            self.state.money += 100
            self.state.energy -= 20
            self.state.stress += 15
        elif action == Action.STUDY:
            self.state.skill_level += 5
            self.state.energy -= 15
            self.state.stress += 5
        elif action == Action.REST:
            self.state.energy += 25
            self.state.stress -= 20
        elif action == Action.SOCIALIZE:
            self.state.happiness += 20
            self.state.stress -= 5
            self.state.energy -= 10

    def _natural_decay(self) -> None:
        self.state.energy -= 2
        self.state.stress += 1
        self.state.happiness -= 1

    def _apply_random_event(self) -> None:
        roll = random.random()
        if roll < 0.05:
            self.state.energy -= 20
            self.state.stress += 20
            self.state.happiness -= 10
        elif roll < 0.1:
            self.state.money += 200
            self.state.happiness += 10

    def _clamp_state(self) -> None:
        self.state.energy = max(0, min(100, self.state.energy))
        self.state.stress = max(0, min(100, self.state.stress))
        self.state.happiness = max(0, min(100, self.state.happiness))
        self.state.skill_level = max(0, self.state.skill_level)
        if self.state.money < 0:
            self.state.money = 0

    def _calculate_reward(self) -> float:
        return (
            self.state.money
            + self.state.happiness
            + self.state.skill_level
            - self.state.stress
            - (100 - self.state.energy)
        )
