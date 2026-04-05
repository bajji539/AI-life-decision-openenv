# AI Life Decision Simulator (OpenEnv + LLM Agent)

A Python-based life decision simulation environment that includes:

- `env/`: life state environment, random events, natural decay, reward logic
- `agents/`: baseline rule-based decision agent
- `tasks/`: easy, medium, hard task definitions
- `grader/`: episode runner, grading, and ASCII graph output
- `inference.py`: OpenAI LLM integration with JSON action parsing and fallback behavior
- `openenv.yaml`: environment metadata for OpenEnv-style task documentation

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
python inference.py
```

## Environment Variables for `inference.py`

- `API_BASE_URL`: Base URL for the OpenAI-compatible API (default: `https://api.openai.com/v1`)
- `MODEL_NAME`: Model to use (default: `gpt-4o-mini`)
- `HF_TOKEN`: OpenAI-style API key
- `OPENAI_API_KEY`: fallback API key if `HF_TOKEN` is not provided
- `LOCAL_IMAGE_NAME`: optional local image name for environment metadata usage

## Goals

- `easy`: survive 30 days
- `medium`: money > 2000, happiness > 50, stress < 70
- `hard`: maximize life score (money + happiness + skill_level - stress)

## Logging

`inference.py` prints logs in the strict format:

```
=== START ===

STEP 0:
state = {...}
action = ...
reward = ...

STEP 1:
...

=== END ===
```
