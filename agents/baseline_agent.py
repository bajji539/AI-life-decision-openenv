from env.models import Action


class BaselineAgent:
    def choose_action(self, state: dict) -> Action:
        energy = state.get("energy", 0)
        stress = state.get("stress", 0)
        skill = state.get("skill_level", 0)

        if energy < 30 or stress > 70:
            return Action.REST
        if skill < 40:
            return Action.STUDY
        return Action.WORK
