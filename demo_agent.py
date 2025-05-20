#!/usr/bin/env python3
"""
Demo Agent using Strands SDK
This script demonstrates how to create a simple agent with custom tools.
"""

from strands import Agent, tool
from typing import List, Dict, Any


@tool
def weather_forecast(city: str, days: int = 3) -> Dict[str, Any]:
    """Get weather forecast for a city.
    
    Args:
        city: The name of the city to get weather for
        days: Number of days for the forecast (default: 3)
        
    Returns:
        A dictionary with weather information
    """
    # In a real implementation, this would call a weather API
    # This is a mock implementation for demonstration
    return {
        "city": city,
        "forecast": [
            {"day": 1, "condition": "Sunny", "temperature": "75°F"},
            {"day": 2, "condition": "Partly Cloudy", "temperature": "72°F"},
            {"day": 3, "condition": "Rainy", "temperature": "65°F"}
        ][:days],
        "humidity": "45%",
        "wind": "5 mph"
    }


@tool
def todo_list(action: str, item: str = None) -> List[str]:
    """Manage a todo list.
    
    Args:
        action: The action to perform (add, list, clear)
        item: The item to add (only required for 'add' action)
        
    Returns:
        The current todo list after the action
    """
    # In a real implementation, this would persist the list
    # This is a simplified version that uses a global variable
    global todos
    
    if not hasattr(todo_list, "todos"):
        todo_list.todos = []
    
    if action == "add" and item:
        todo_list.todos.append(item)
    elif action == "clear":
        todo_list.todos = []
    
    return todo_list.todos


def main():
    """Run the demo agent."""
    # Create an agent with our custom tools
    agent = Agent(tools=[weather_forecast, todo_list])
    
    print("Demo Agent initialized with custom tools.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Process the user input with the agent
        response = agent(user_input)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    print("Starting Strands Demo Agent...")
    print("Note: This requires the strands-agents package to be installed.")
    print("Install with: pip install strands-agents")
    main()
