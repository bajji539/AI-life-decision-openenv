from typing import Any

from env.models import Action


class Grader:
    def run_episode(self, env: Any, agent: Any, max_steps: int = 30) -> list[dict]:
        history = []
        env.reset()
        for step in range(max_steps):
            state = env.get_observation()
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            history.append(
                {
                    "step": step,
                    "state": state,
                    "action": str(action),
                    "reward": reward,
                    "next_state": next_state,
                    "done": done,
                }
            )
            if done:
                break
        return history

    def grade(self, history: list[dict], goal_func=None, score_func=None) -> dict:
        final_state = history[-1]["next_state"] if history else {}
        total_reward = sum(entry["reward"] for entry in history)
        result = {
            "steps": len(history),
            "total_reward": total_reward,
            "final_state": final_state,
        }
        if goal_func is not None:
            result["success"] = goal_func(final_state)
        if score_func is not None:
            result["normalized_score"] = score_func(final_state)
        return result

    def print_ascii_graphs(self, history: list[dict]) -> None:
        print("\nASCII GRAPHS")
        if not history:
            print("No history to render.")
            return

        keys = ["energy", "stress", "happiness", "money", "skill_level"]
        for key in keys:
            values = [entry["state"].get(key, 0) for entry in history]
            self._print_graph(key, values)

    def _print_graph(self, label: str, values: list[int]) -> None:
        bars = ["=" * (max(0, min(50, int(value / max(1, max(values))) * 50 // 50))) for value in values]
        print(f"{label.upper():>12}: ")
        for index, bar in enumerate(bars):
            print(f" {index:02d}: {bar}")
