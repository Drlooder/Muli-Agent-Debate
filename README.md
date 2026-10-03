# Multi-Agent Debate System

A real-time multi-agent AI debate framework for orchestrating structured conversations between autonomous language agents. The project is designed to simulate intellectual debate, role-based reasoning, and collaborative or adversarial decision making in a controlled environment.

This repository combines:
- Python for backend orchestration and agent logic
- HTML, CSS, and JavaScript for the user-facing interface
- LLM-powered agents for reasoning, rebuttal, and synthesis

## Overview

The system allows multiple AI agents to participate in a shared debate around a topic or problem. Each agent can be assigned a role, perspective, or strategy, and the platform coordinates their responses in a structured sequence.

Common use cases include:
- multi-agent reasoning
- debate simulation
- collaborative decision support
- adversarial evaluation of ideas
- research on agent communication and consensus-building

## Core Concepts

The application is built around a few essential ideas:

- Agent roles: each participant has a specialized perspective or behavior
- Debate loop: agents respond in sequence or rounds
- Orchestration layer: manages turn flow, timing, and conversation state
- Context memory: tracks previous arguments and discussion progression
- Final synthesis: combines arguments into a conclusion or summary

## Features

- Multi-agent debate orchestration
- Role-based agent behavior
- Structured conversation flow
- Real-time argument exchange
- Rebuttal and synthesis supported by the debate engine
- Extensible agent architecture
- Browser-based interface for user interaction
- Configurable model and prompt behavior

## Architecture

The project is organized around a simple architecture:

- Frontend: web interface for starting debates and viewing outputs
- Backend: Python services that manage agent coordination
- Debate engine: controls rounds, context, roles, and final evaluation
- LLM integration: sends prompts to the model(s) used by agents
- State management: tracks conversation flow and generation history

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher** — [Download Python](https://www.python.org/downloads/)
- **pip** — Python package manager (usually included with Python)
- **Git** — [Download Git](https://git-scm.com/)
- **A modern web browser** — Chrome, Firefox, Safari, or Edge
- **API key** — [Groq Api Keys](https://console.groq.com/)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Drlooder/Muli-Agent-Debate.git
cd Muli-Agent-Debate
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to isolate dependencies.

**On macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**

```bash
python -m venv venv
venv\Scripts\activate
```

**On Windows (PowerShell):**

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Once activated, you should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

Install the required Python packages from `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
cp .env.example .env
```

Then open `.env` in your text editor and add your configuration:

```env
# LLM Configuration
GROQ_API_KEY="your_key_here"
SECRET_KEY_FALSK="whatevet"
```
Replace `your_openai_api_key_here` with your actual API key from your LLM provider.

### Step 5: Run the Application

Start the application:

```bash
python main.py
```

Or if using Flask:

```bash
flask run
```

The application should now be running at `http://localhost:5000` (or the configured port).

### Step 6: Access the Web Interface

Open your web browser and navigate to:

```
http://localhost:5000
```

You should see the Multi-Agent Debate System interface.

## Troubleshooting Installation

### Issue: Command not found: `python3`

**Solution:** Make sure Python is installed and added to your system PATH. Try `python` instead of `python3`.

### Issue: Permission denied when activating virtual environment

**Solution:** On Windows, run PowerShell as Administrator or use Command Prompt instead. On macOS/Linux, ensure the file is executable:

```bash
chmod +x venv/bin/activate
```

### Issue: ModuleNotFoundError when running the app

**Solution:** Ensure your virtual environment is activated and all dependencies are installed:

```bash
pip install -r requirements.txt
```

### Issue: API key not recognized

**Solution:** Double-check that your `.env` file is in the project root and contains the correct API key. Restart the application after updating `.env`.

## Usage

1. Launch the application and open the web interface.
2. Enter a debate topic or prompt in the input field.
3. Configure the participating agents (roles, strategies, etc.).
4. Click "Start Debate" to begin the discussion.
5. Monitor the real-time argument exchange between agents.
6. Review the final summary or verdict generated by the system.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m "Add your feature"`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Support

For issues, questions, or feature requests, please open an issue on the [GitHub Issues](https://github.com/Drlooder/Muli-Agent-Debate/issues) page.

## Contact

For more information, visit the project repository or contact the maintainer.
