# Agentic Workflows

This repository contains examples of different agentic patterns and workflows.

## Projects

* **[Prompt Chaining](prompt-chaining/README.md)**: A sequential prompt workflow integrated with a local JSON database and validation lookup, using a free Gemini API key through the standard OpenAI compatible client.
* **[Routing Pattern](routing/README.md)**: An agentic workflow that uses a Router AI to classify incoming user requests and dispatch them to specialized specialist prompts (Billing, Tech Support, or Returns) backed by a local JSON database lookup.
* **[Parallelization](parallelization/README.md)**: An agentic workflow that runs multiple specialized auditor agents (Security, Performance, Style) in parallel to review a Pull Request, and then synthesizes their feedback into a single consolidated review comment.
* **[Orchestrator-Workers](orchestrator-workers/README.md)**: An agentic workflow where a central Orchestrator plans and delegates specialized tasks to multiple Worker agents (Index Funds, Real Estate, and Tax Pros/Cons) in parallel, then synthesizes their findings into a single consolidated recommendation.


## ⚙️ Setup & Installation

### 1. Configure the Environment
Clone this repository and create a `.env` file in the project root:
```env
# Get a free Gemini API key from https://aistudio.google.com/
GEMINI_API_KEY=your_actual_api_key_here
```

### 2. Install Dependencies
Make sure you have python installed and run:
```bash
pip install -r requirements.txt
```
