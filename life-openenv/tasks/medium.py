def medium_goal(state: dict) -> bool:
    """Check if agent reached all objectives."""
    return (
        state.get("money", 0) > 2000
        and state.get("happiness", 0) > 50
        and state.get("stress", 100) < 70
    )


def medium_score(state: dict) -> float:
    """Calculate normalized score (0.0-1.0) for medium task."""
    money_score = min(state.get("money", 0) / 2000.0, 1.0)
    happiness_score = max(0, min((state.get("happiness", 0) - 50) / 50.0, 1.0))
    stress_score = max(0, (70 - state.get("stress", 100)) / 70.0)
    return (money_score + happiness_score + stress_score) / 3.0


def medium_description() -> str:
    return "Reach money > 2000, happiness > 50, and stress < 70. Score: weighted average of normalized metrics"
