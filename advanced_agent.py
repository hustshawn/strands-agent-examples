#!/usr/bin/env python3
"""
Advanced Agent using Strands SDK
This script demonstrates more advanced features of the Strands SDK.
"""

from strands import Agent, tool
from strands.types import AgentConfig
from typing import List, Dict, Any, Optional


@tool
def search_database(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Search a database for information.
    
    Args:
        query: The search query
        limit: Maximum number of results to return
        
    Returns:
        A list of search results
    """
    # Mock implementation
    results = [
        {"id": 1, "title": "Introduction to AI Agents", "content": "AI agents are software entities that can perceive their environment and take actions."},
        {"id": 2, "title": "Strands SDK Overview", "content": "Strands is a model-driven approach to building AI agents in just a few lines of code."},
        {"id": 3, "title": "Building Custom Tools", "content": "Custom tools allow agents to interact with external systems and APIs."},
        {"id": 4, "title": "Multi-Agent Systems", "content": "Multiple agents can work together to solve complex problems."},
        {"id": 5, "title": "Agent Memory", "content": "Agents can maintain state and memory across interactions."}
    ]
    
    filtered_results = [r for r in results if query.lower() in r["title"].lower() or query.lower() in r["content"].lower()]
    return filtered_results[:limit]


@tool
def calculate(expression: str) -> float:
    """Calculate the result of a mathematical expression.
    
    Args:
        expression: The mathematical expression to evaluate
        
    Returns:
        The result of the calculation
    """
    # Note: eval is used for demonstration only
    # In production, use a safer approach for expression evaluation
    try:
        return float(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error: {str(e)}"


class KnowledgeBase:
    """A simple knowledge base for the agent to use."""
    
    def __init__(self):
        self.facts = {
            "strands": "A model-driven approach to building AI agents",
            "agent": "A software entity that can perceive and act",
            "tool": "A function that an agent can use to interact with systems"
        }
    
    def get_fact(self, key: str) -> Optional[str]:
        """Get a fact from the knowledge base."""
        return self.facts.get(key.lower())
    
    def add_fact(self, key: str, value: str) -> None:
        """Add a fact to the knowledge base."""
        self.facts[key.lower()] = value


@tool
def knowledge_lookup(key: str) -> str:
    """Look up information in the knowledge base.
    
    Args:
        key: The key to look up
        
    Returns:
        The information if found, otherwise a message indicating it wasn't found
    """
    if not hasattr(knowledge_lookup, "kb"):
        knowledge_lookup.kb = KnowledgeBase()
    
    result = knowledge_lookup.kb.get_fact(key)
    return result if result else f"No information found for '{key}'"


@tool
def knowledge_add(key: str, value: str) -> str:
    """Add information to the knowledge base.
    
    Args:
        key: The key to add
        value: The value to associate with the key
        
    Returns:
        A confirmation message
    """
    if not hasattr(knowledge_lookup, "kb"):
        knowledge_lookup.kb = KnowledgeBase()
    
    knowledge_lookup.kb.add_fact(key, value)
    return f"Added information about '{key}'"


def main():
    """Run the advanced agent."""
    # Configure the agent with custom settings
    config = AgentConfig(
        temperature=0.3,  # Lower temperature for more deterministic responses
        max_tokens=1000,  # Limit response length
    )
    
    # Create an agent with our custom tools and configuration
    agent = Agent(
        tools=[search_database, calculate, knowledge_lookup, knowledge_add],
        config=config
    )
    
    print("Advanced Agent initialized with custom tools and configuration.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Process the user input with the agent
        response = agent(user_input)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    print("Starting Strands Advanced Agent...")
    print("Note: This requires the strands-agents package to be installed.")
    print("Install with: pip install strands-agents")
    main()
