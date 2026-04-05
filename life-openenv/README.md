# AI Life Decision Simulator (OpenEnv + LLM Agent)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive Python-based life decision simulation environment that models human daily choices using reinforcement learning principles. Features a baseline rule-based agent and integration with Large Language Models (LLMs) for intelligent decision-making.

## 🚀 Features

- **Realistic Life Simulation**: Model energy, stress, money, happiness, and skill levels with natural decay and random events
- **Multiple Agents**: Rule-based baseline agent and LLM-powered agent using OpenAI API
- **Flexible Interface**: Choose between terminal output or interactive GUI
- **Structured Tasks**: Easy, medium, and hard difficulty levels with clear objectives
- **OpenEnv Compatible**: YAML configuration for environment metadata
- **Robust Logging**: Strict log format for analysis and debugging
- **Fallback Mechanisms**: Graceful handling when LLM services are unavailable

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
- [Logging Format](#logging-format)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Installation

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/ai-life-decision-simulator.git
cd ai-life-decision-simulator/life-openenv

# Create virtual environment
python -m venv ../.venv

# Activate virtual environment
# On Windows:
../.venv/Scripts/Activate.ps1
# On macOS/Linux:
# source ../.venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

Run the interactive GUI interface:
```bash
python interface.py
```

Choose between Terminal or GUI mode, enter your API credentials, and watch the simulation unfold!

## 📖 Usage

### GUI Mode (Recommended)
```bash
python interface.py
```
- Interactive prompts for mode selection and environment variables
- Real-time display of simulation steps in a scrollable window
- Logs also printed to console

### Terminal Mode
```bash
python main.py        # Run baseline agent tasks
python inference.py   # Run LLM-powered simulation
```

### Command Line Options
The interface will prompt for:
1. **Mode**: Terminal (1) or GUI (2)
2. **API_BASE_URL**: OpenAI-compatible API endpoint
3. **MODEL_NAME**: LLM model to use
4. **HF_TOKEN**: API key for authentication
5. **LOCAL_IMAGE_NAME**: Optional Docker image name

## 🔧 Environment Variables

Configure these variables for LLM functionality:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `API_BASE_URL` | OpenAI-compatible API endpoint | `https://api.openai.com/v1` | No |
| `MODEL_NAME` | LLM model name | `gpt-4o-mini` | No |
| `HF_TOKEN` | API authentication token | None | Yes* |
| `OPENAI_API_KEY` | Alternative API key | None | Yes* |
| `LOCAL_IMAGE_NAME` | Docker image identifier | None | No |

*Required for LLM features; falls back to rule-based agent if not provided

## 📁 Project Structure

```
life-openenv/
│
├── env/
│   ├── __init__.py
│   ├── models.py          # Action and LifeState dataclasses
│   ├── environment.py     # Core simulation logic
│   └── generator.py       # Random action generator
│
├── agents/
│   ├── __init__.py
│   └── baseline_agent.py  # Rule-based decision agent
│
├── tasks/
│   ├── __init__.py
│   ├── easy.py            # Easy task: survive 30 days
│   ├── medium.py          # Medium task: achieve financial/happiness goals
│   └── hard.py            # Hard task: maximize life score
│
├── grader/
│   ├── __init__.py
│   └── grader.py          # Episode runner and ASCII graph generator
│
├── inference.py           # LLM integration script
├── main.py               # Baseline agent runner
├── interface.py          # GUI/terminal interface
├── openenv.yaml          # Environment metadata
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎯 Tasks

### Easy Task
**Objective**: Survive 30 days with the life state intact
- Simple survival challenge
- Tests basic agent stability

### Medium Task
**Objective**: Reach money > 2000, happiness > 50, and stress < 70
- Balanced achievement goals
- Requires strategic decision-making

### Hard Task
**Objective**: Maximize life score (money + happiness + skill_level - stress)
- Complex optimization problem
- Challenges advanced planning

## 📝 Logging Format

All simulations output logs in this exact format:

```
=== START ===

STEP 0:
state = {'energy': 80, 'stress': 20, 'money': 500, 'happiness': 50, 'skill_level': 10, 'day': 0}
action = REST
reward = 558

STEP 1:
state = {'energy': 100, 'stress': 1, 'money': 500, 'happiness': 49, 'skill_level': 10, 'day': 1}
action = REST
reward = 546

...

=== END ===
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt  # If available

# Run tests
python -m pytest

# Format code
black .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with OpenAI API for LLM integration
- Inspired by reinforcement learning environments like OpenAI Gym
- Uses Tkinter for cross-platform GUI functionality

---

**Enjoy simulating life decisions!** 🎮

STEP 1:
...

=== END ===
```
