def easy_goal(state: dict) -> bool:
    """Check if agent survived 30 days."""
    return state.get("day", 0) >= 30


def easy_score(state: dict) -> float:
    """Calculate normalized score (0.0-1.0) for easy task."""
    days = min(state.get("day", 0), 30)
    return days / 30.0


def easy_description() -> str:
    return "Survive 30 days with the life state intact. Score: days_survived / 30"
