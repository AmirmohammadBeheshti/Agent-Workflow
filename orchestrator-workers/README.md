# 🤝 Orchestrator-Workers Workflow (Dynamic Wealth Strategy Planner)

The **Orchestrator-Workers Pattern** is an agentic workflow where a central "Orchestrator" LLM agent breaks down a complex user prompt into specific, independent sub-tasks, dispatches these sub-tasks to multiple specialized "Worker" agents, and then synthesizes their independent responses into a single, cohesive, and comprehensive final output.

In this directory, we implement **Option 2: Dynamic Roles (Orchestrator Decides at Runtime)**. Instead of using hardcoded specialists, the Orchestrator dynamically plans which specialists are required based on the user's specific request.

---

## 🏗️ Architecture

```
                  ┌──────────────────────┐
                  │     ORCHESTRATOR     │
                  │  (Dynamically Plans  │
                  │   Worker Roles in    │
                  │    Structured JSON)  │
                  └──────────┬───────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ DYNAMIC WORKER  │ │ DYNAMIC WORKER  │ │ DYNAMIC WORKER  │
│    Persona A    │ │    Persona B    │ │    Persona C    │
│  (e.g., Crypto) │ │ (e.g., Gold)    │ │  (e.g., Bonds)  │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             ▼
                  ┌──────────────────────┐
                  │     ORCHESTRATOR     │
                  │   (Synthesizes)      │
                  └──────────────────────┘
```

The workflow operates in three steps:

1.  **Dynamic Role Planning**:
    The Orchestrator reviews the user's raw query and returns a structured JSON list of 2–3 custom worker roles tailored specifically to the assets, risks, or topics mentioned. Each planned worker has a custom name, specialized system instruction (defining their persona), and a custom target prompt.
    
2.  **Parallel Worker Execution**:
    The Orchestrator instantiates generic Worker agents, configures them with the dynamically planned personas and instructions, and runs them concurrently in threads using Python's `ThreadPoolExecutor`.
    
3.  **Synthesis**:
    The Orchestrator receives all worker reports, resolves any conflicting advice, and compiles them into a unified wealth proposal containing an Executive Summary, proposed asset allocation percentages, pros/cons, tax strategies, and next steps.

---

## 📁 Repository Structure

- `orchestrator-workers.ipynb`: The interactive Jupyter Notebook containing the Gemini client initialization, dynamic role planner prompt, parallel threading execution loop, and synthesis engine.
