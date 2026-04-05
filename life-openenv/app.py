import gradio as gr
import json
import os
import random

from env.environment import LifeEnvironment
from env.models import Action

# Environment variables (set in HF Space secrets or here)
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")  # Set in HF Space secrets

def setup_client():
    if HF_TOKEN:
        from openai import OpenAI
        return OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)
    return None

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
    except:
        return Action.REST

def choose_llm_action(client, state: dict) -> Action:
    if client is None:
        return Action.REST
    prompt = build_prompt(state)
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
        )
        raw_text = response.choices[0].message.content.strip()
        return parse_action(raw_text)
    except:
        return Action.REST

def run_simulation(use_llm: bool, max_steps: int = 20):
    random.seed(42)
    env = LifeEnvironment()
    env.reset()
    client = setup_client() if use_llm else None

    log_lines = ["=== START ==="]
    for step in range(max_steps):
        state = env.get_observation()
        action = choose_llm_action(client, state) if use_llm else Action.REST  # Simple fallback
        next_state, reward, done = env.step(action)
        step_log = f"\nSTEP {step}:\nstate = {state}\naction = {action}\nreward = {reward}"
        log_lines.append(step_log)
        if done:
            break
    log_lines.append("=== END ===")

    return "\n".join(log_lines)

def gradio_interface(use_llm, max_steps):
    return run_simulation(use_llm, int(max_steps))

# Gradio Interface
with gr.Blocks(title="AI Life Decision Simulator") as demo:
    gr.Markdown("# AI Life Decision Simulator")
    gr.Markdown("Simulate life decisions with AI or baseline agent.")

    with gr.Row():
        use_llm = gr.Checkbox(label="Use LLM Agent (requires API key)", value=False)
        max_steps = gr.Slider(minimum=5, maximum=50, value=20, step=1, label="Max Steps")

    run_btn = gr.Button("Run Simulation")
    output = gr.Textbox(label="Simulation Log", lines=30, interactive=False)

    run_btn.click(gradio_interface, inputs=[use_llm, max_steps], outputs=output)

if __name__ == "__main__":
    demo.launch()