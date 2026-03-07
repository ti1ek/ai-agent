# AI Agent from Scratch

A minimal AI agent built from scratch using OpenAI's API with tool-calling capabilities. This project demonstrates the core concepts behind AI agents — maintaining conversation history, defining tools, and letting the model decide when to call them.

## How It Works

The agent runs in an interactive loop where:

1. The user sends a message
2. The message is forwarded to OpenAI's GPT-4o-mini model
3. If the model decides to call a tool, the agent executes it and feeds the result back
4. The model generates a final response incorporating the tool's output

```
User → Agent → OpenAI API → Tool Call? → Execute Tool → Response
                    ↑                                       |
                    └───────────────────────────────────────┘
```

## Features

- **Conversational memory** — maintains full message history across turns
- **Tool calling** — defines tools as JSON schemas that the model can invoke
- **Extensible** — add new tools by defining a function and registering it in `FUNCTION_MAP` and `TOOLS`

## Example

```
You: what is the weather in Spain?
Calling function: get_weather with {"city":"Spain"}
AI: The weather in Spain is currently 33 degrees Celsius.
```

## Project Structure

```
├── main.ipynb        # Main notebook with agent implementation
├── pyproject.toml    # Project config and dependencies
├── .env              # API keys (not committed)
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager
- OpenAI API key

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/ai-agent-from-scratch.git
cd ai-agent-from-scratch

# Install dependencies
uv sync

# Add your OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env

# Run the notebook
jupyter notebook main.ipynb
```

## Dependencies

- `openai` — OpenAI Python SDK
- `ipykernel` — Jupyter kernel (dev)

## License

MIT
