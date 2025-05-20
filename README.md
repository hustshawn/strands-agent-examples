# Strands Agents Demo

This repository contains demo implementations using the Strands Agents SDK, a model-driven approach to building AI agents in just a few lines of code.

## Prerequisites

Before running these demos, you need to install the Strands Agents SDK:

```bash
pip install strands-agents strands-agents-tools
```

For the default Amazon Bedrock model provider, you'll need AWS credentials configured and model access enabled for Claude 3.7 Sonnet in the us-west-2 region. See the [Quickstart Guide](https://strandsagents.com/) for details on configuring other model providers.

## Demo Scripts

This repository includes three demo scripts:

### 1. Basic Demo Agent (`demo_agent.py`)

A simple agent with two custom tools:
- Weather forecast tool
- Todo list management tool

Run with:
```bash
python demo_agent.py
```

### 2. Advanced Agent (`advanced_agent.py`)

A more advanced agent with:
- Database search tool
- Calculator tool
- Knowledge base lookup and addition tools
- Custom agent configuration

Run with:
```bash
python advanced_agent.py
```

### 3. Multi-Agent System (`multi_agent_system.py`)

A system with multiple specialized agents:
- Research agent with web search capability
- Summary agent for text summarization
- Coordinator agent that delegates tasks to specialized agents

Run with:
```bash
python multi_agent_system.py
```

## Example Usage

Here are some example prompts you can try with the demo agents:

### Basic Demo Agent
- "What's the weather like in Seattle?"
- "Add buy groceries to my todo list"
- "Show me my todo list"
- "Clear my todo list"

### Advanced Agent
- "Search for information about AI agents"
- "Calculate 15 * 7 + 22"
- "What do you know about strands?"
- "Add a fact: LLM stands for Large Language Model"
- "What is an LLM?"

### Multi-Agent System
- "Research quantum computing"
- "Summarize this article: [paste a long article here]"
- "Find information about climate change and summarize it"

## Additional Resources

- [Strands Agents Documentation](https://strandsagents.com/)
- [GitHub Repository](https://github.com/strands-agents/sdk-python)
- [Examples](https://github.com/strands-agents/docs/tree/main/docs/examples)
- [Tools](https://github.com/strands-agents/tools)
- [Agent Builder](https://github.com/strands-agents/agent-builder)
