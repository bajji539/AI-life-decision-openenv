def easy_goal(state: dict) -> bool:
    return state.get("day", 0) >= 30


def easy_description() -> str:
    return "Survive 30 days with the life state intact."
