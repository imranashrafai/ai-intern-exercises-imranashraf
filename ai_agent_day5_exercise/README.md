# Day 5 — Simple AI Agent with Tools (Gemini)

This project implements a **Simple AI Agent** using the Gemini API.  
The goal of this assignment is to understand how **Large Language Models (LLMs)** can interact with **external tools** to solve problems through reasoning and actions.

Instead of answering every query directly, the agent can:

- Analyze the user query
- Decide whether a tool is required
- Execute the tool
- Use the tool result to generate the final response

This demonstrates the core idea behind modern **AI agent systems**.

---

# Objective

Build a simple AI assistant that can:

- Answer conceptual questions directly
- Use a **calculator tool** for mathematical problems
- Retrieve information using **Wikipedia**
- Perform **web search queries**
- Fetch **weather information for cities**
- Print **REACT-style reasoning**
- Save queries and results to files

---

# Agent Workflow

The agent follows a simplified **REACT-style reasoning loop**:

```
User Query
   ↓
LLM Reasoning
   ↓
Tool Selection
   ↓
Tool Execution
   ↓
Observation
   ↓
Final Answer
```

This workflow demonstrates how modern **AI agent systems combine reasoning with external tools**.

---

# Tools Implemented

## 1. Calculator Tool

Performs mathematical calculations.

Example:

```
Input: 25 * 8
Output: 200
```

---

## 2. Wikipedia Tool

Retrieves short summaries from Wikipedia for informational queries.

Example:

```
Input: Alan Turing
Output: Short Wikipedia summary about Alan Turing
```

---

## 3. Search Tool

Performs general web searches to retrieve factual information.

Example:

```
Input: capital of Canada
Output: Ottawa is the capital of Canada
```

---

## 4. Weather Tool

Fetches current weather information for a given city.

Example:

```
Input: Tokyo
Output: Current temperature in Tokyo
```

---

# REACT Reasoning Example

The agent prints reasoning steps similar to the REACT framework:

```
Thought: The user asked a math question
Action: calculator
Action Input: 25 * 8
Observation: 200
Final Answer: 25 multiplied by 8 equals 200
```

This shows how the model **reasons before performing an action**.

---

# Project Structure

```
ai-intern-exercises/
└── day5_simple_agent/
    ├── agent.py
    ├── tools.py
    ├── queries.txt
    └── results.txt
```

**agent.py**

Main implementation of the AI agent.

**tools.py**

Contains the external tools used by the agent:
- calculator
- wikipedia
- search
- weather

**queries.txt**

Stores test queries executed during runtime.

**results.txt**

Stores the outputs produced by the agent.

---

# Installation

Install the required dependencies:

```
pip install google-generativeai python-dotenv wikipedia requests
```

---

# Environment Setup

Create a `.env` file in the project directory and add your Gemini API key.

```
GEMINI_API_KEY=your_api_key_here
```

Important:  
The `.env` file should **not be committed** to version control.

---

# Running the Agent

Navigate to the project directory and run:

```
python agent.py
```

Example interaction:

```
User: What is 12 * 7?

Thought: The user asked a math question
Action: calculator
Observation: 84

Final Answer:
12 multiplied by 7 equals 84
```

---

# Example Queries

The following queries were used to test the agent:

```
What is 12 * 7?
What is 100 / 5?
Explain what embeddings are.
Who is Alan Turing?
What is the weather in Tokyo?
```

---

# Example Output

Example entry from `results.txt`:

```
Query: What is 12 * 7?
Tool used: calculator
Answer:
12 multiplied by 7 equals 84.
---

Query: Explain what embeddings are.
Tool used: none
Answer:
Embeddings are numerical vector representations of text that capture semantic meaning.
---
```

---

# Key Concepts Learned

## AI Agents
Systems where LLMs can reason and perform actions.

## Tool Integration
Allows LLMs to interact with external APIs or functions.

## REACT Framework
Reason → Act → Observe → Respond loop used in agent systems.

## Prompt-Based Tool Selection
The model decides when a tool should be used.

---

# Summary

This assignment demonstrates how a **tool-enabled AI agent** can extend the capabilities of a language model by allowing it to:

- Perform reasoning before answering
- Select appropriate tools
- Execute external functions
- Combine tool outputs with generated responses

These concepts are fundamental for building modern **AI assistants and autonomous agents**.