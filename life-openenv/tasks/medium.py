def medium_goal(state: dict) -> bool:
    return (
        state.get("money", 0) > 2000
        and state.get("happiness", 0) > 50
        and state.get("stress", 100) < 70
    )


def medium_description() -> str:
    return "Reach money > 2000, happiness > 50, and stress < 70."
