def hard_score(state: dict) -> float:
    """Calculate normalized score (0.0-1.0) for hard task."""
    # Raw score: money + happiness + skill_level - stress
    raw_score = (
        state.get("money", 0)
        + state.get("happiness", 0)
        + state.get("skill_level", 0)
        - state.get("stress", 0)
    )
    # Normalize to 0.0-1.0 range (max realistic score ~5000)
    normalized = min(raw_score / 5000.0, 1.0)
    return max(0.0, normalized)


def hard_description() -> str:
    return "Maximize life score = money + happiness + skill_level - stress. Score: raw_score / 5000"
