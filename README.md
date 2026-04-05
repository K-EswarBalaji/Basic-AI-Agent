# Basic AI Agent

A Python-based AI agent project demonstrating basic agent functionality.

## Project Structure

```
├── agents/
│   └── ai-agent-1/
│       ├── __init__.py
│       ├── agent.py
│       └── requirements.txt
├── __init__.py
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/K-EswarBalaji/Basic-AI-Agent.git
cd Basic-AI-Agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
cd agents/ai-agent-1
pip install -r requirements.txt
```

## Usage

To run the agent:
```bash
python agents/ai-agent-1/agent.py
```

## Environment Variables

Create a `.env` file in the root directory with your configuration:
```
API_KEY=your_api_key_here
```

**Note:** The `.env` file is ignored by git for security purposes.

## License

This project is open source and available under the MIT License.

## Author

K. Eswar Balaji
