import json
import os
import random

from openai import OpenAI

from env.environment import LifeEnvironment
from env.models import Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")
OPENAI_API_KEY = HF_TOKEN or os.getenv("OPENAI_API_KEY")
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

client = None

if OPENAI_API_KEY:
    client = OpenAI(
        base_url=API_BASE_URL,
        api_key=OPENAI_API_KEY,
    )

FALLBACK_ACTION = Action.REST


def build_prompt(state: dict) -> str:
    return (
        "You are an agent deciding a human's next life action. "
        "Use only one of: WORK, STUDY, REST, SOCIALIZE. "
        f"Current state: {json.dumps(state)}. "
        "Return only valid JSON with the format {\"action\": \"WORK\"}."
    )


def parse_action(response_text: str) -> Action:
    try:
        parsed = json.loads(response_text.strip())
        action_value = parsed.get("action", "REST").upper()
        return Action(action_value)
    except (json.JSONDecodeError, ValueError, TypeError):
        return FALLBACK_ACTION


def choose_llm_action(state: dict) -> Action:
    if client is None:
        return FALLBACK_ACTION

    prompt = build_prompt(state)
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
        )
        raw_text = response.choices[0].message.content.strip()
        return parse_action(raw_text)
    except Exception:
        return FALLBACK_ACTION


def inference_loop(max_steps: int = 20) -> None:
    random.seed(42)
    env = LifeEnvironment()
    env.reset()

    print("=== START ===")
    for step in range(max_steps):
        state = env.get_observation()
        action = choose_llm_action(state)
        next_state, reward, done = env.step(action)
        print(f"\nSTEP {step}:")
        print(f"state = {state}")
        print(f"action = {action}")
        print(f"reward = {reward}")
        if done:
            break
    print("=== END ===")


if __name__ == "__main__":
    inference_loop()
