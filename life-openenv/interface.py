import json
import os
import random
import subprocess
import sys
import tkinter as tk
from tkinter import simpledialog, scrolledtext

from openai import OpenAI

from env.environment import LifeEnvironment
from env.models import Action

# Environment variables with defaults
DEFAULT_API_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL_NAME = "gpt-4o-mini"

def get_env_vars():
    api_base = simpledialog.askstring("API_BASE_URL", "Enter API_BASE_URL:", initialvalue=DEFAULT_API_BASE_URL)
    model_name = simpledialog.askstring("MODEL_NAME", "Enter MODEL_NAME:", initialvalue=DEFAULT_MODEL_NAME)
    hf_token = simpledialog.askstring("HF_TOKEN", "Enter HF_TOKEN (leave empty if none):")
    local_image_name = simpledialog.askstring("LOCAL_IMAGE_NAME", "Enter LOCAL_IMAGE_NAME (leave empty if none):")
    return api_base, model_name, hf_token, local_image_name

def setup_client(api_base, model_name, hf_token):
    client = None
    if hf_token:
        client = OpenAI(
            base_url=api_base,
            api_key=hf_token,
        )
    return client

def build_prompt(state: dict) -> str:
    return (
        "You are an agent deciding a human's next life action. "
        "Use only one of: WORK, STUDY, REST, SOCIALIZE. "
        f"Current state: {json.dumps(state)}. "
        "Return only valid JSON with the format {{\"action\": \"WORK\"}}."
    )

def parse_action(response_text: str) -> Action:
    try:
        parsed = json.loads(response_text.strip())
        action_value = parsed.get("action", "REST").upper()
        return Action(action_value)
    except (json.JSONDecodeError, ValueError, TypeError):
        return Action.REST

def choose_llm_action(client, model_name, state: dict) -> Action:
    if client is None:
        return Action.REST

    prompt = build_prompt(state)
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
        )
        raw_text = response.choices[0].message.content.strip()
        return parse_action(raw_text)
    except Exception:
        return Action.REST

def run_simulation(client, model_name, max_steps=20, gui_text=None):
    random.seed(42)
    env = LifeEnvironment()
    env.reset()

    log_lines = ["=== START ==="]
    for step in range(max_steps):
        state = env.get_observation()
        action = choose_llm_action(client, model_name, state)
        next_state, reward, done = env.step(action)
        step_log = f"\nSTEP {step}:\nstate = {state}\naction = {action}\nreward = {reward}"
        log_lines.append(step_log)
        if done:
            break
    log_lines.append("=== END ===")

    full_log = "\n".join(log_lines)
    print(full_log)
    if gui_text:
        gui_text.insert(tk.END, full_log + "\n")
        gui_text.see(tk.END)

def terminal_mode():
    api_base, model_name, hf_token, local_image_name = get_env_vars()
    os.environ['API_BASE_URL'] = api_base
    os.environ['MODEL_NAME'] = model_name
    if hf_token:
        os.environ['HF_TOKEN'] = hf_token
    if local_image_name:
        os.environ['LOCAL_IMAGE_NAME'] = local_image_name

    client = setup_client(api_base, model_name, hf_token)
    run_simulation(client, model_name)

def gui_mode():
    api_base, model_name, hf_token, local_image_name = get_env_vars()
    os.environ['API_BASE_URL'] = api_base
    os.environ['MODEL_NAME'] = model_name
    if hf_token:
        os.environ['HF_TOKEN'] = hf_token
    if local_image_name:
        os.environ['LOCAL_IMAGE_NAME'] = local_image_name

    client = setup_client(api_base, model_name, hf_token)

    # Create GUI window
    gui_root = tk.Tk()
    gui_root.title("AI Life Decision Simulator - GUI Mode")
    gui_root.geometry("800x600")

    text_area = scrolledtext.ScrolledText(gui_root, wrap=tk.WORD, width=100, height=30)
    text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Run simulation in GUI
    run_simulation(client, model_name, gui_text=text_area)

    gui_root.mainloop()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    mode = simpledialog.askinteger(
        "Select Mode",
        "Choose mode:\n1. Terminal\n2. GUI",
        minvalue=1,
        maxvalue=2
    )

    if mode == 1:
        terminal_mode()
    elif mode == 2:
        gui_mode()
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()