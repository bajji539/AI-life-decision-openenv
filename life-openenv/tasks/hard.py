def hard_score(state: dict) -> int:
    return (
        state.get("money", 0)
        + state.get("happiness", 0)
        + state.get("skill_level", 0)
        - state.get("stress", 0)
    )


def hard_description() -> str:
    return "Calculate life score = money + happiness + skill_level - stress."
