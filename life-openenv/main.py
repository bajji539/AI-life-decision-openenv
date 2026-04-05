import random

from env.environment import LifeEnvironment
from agents.baseline_agent import BaselineAgent
from grader.grader import Grader
from tasks.easy import easy_goal, easy_description
from tasks.medium import medium_goal, medium_description
from tasks.hard import hard_score, hard_description


def run_task(name: str, env: LifeEnvironment, agent: BaselineAgent, grader: Grader, max_steps: int = 30):
    print(f"\n=== RUNNING {name.upper()} TASK ===")
    history = grader.run_episode(env, agent, max_steps=max_steps)
    if name == "easy":
        result = grader.grade(history, easy_goal)
        print(f"Task: {easy_description()}")
    elif name == "medium":
        result = grader.grade(history, medium_goal)
        print(f"Task: {medium_description()}")
    else:
        result = grader.grade(history)
        result["score"] = hard_score(result["final_state"])
        result["success"] = result["score"] is not None
        print(f"Task: {hard_description()}")

    print("Result:", result)
    grader.print_ascii_graphs(history)
    return history


def main() -> None:
    random.seed(42)
    env = LifeEnvironment()
    agent = BaselineAgent()
    grader = Grader()

    run_task("easy", env, agent, grader, max_steps=30)
    run_task("medium", env, agent, grader, max_steps=50)
    run_task("hard", env, agent, grader, max_steps=50)


if __name__ == "__main__":
    main()
