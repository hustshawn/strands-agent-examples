#!/usr/bin/env python3
"""
Multi-Agent System using Strands SDK
This script demonstrates how to create a system with multiple specialized agents.
"""

from strands import Agent, tool
from typing import Dict, Any, List


@tool
def web_search(query: str) -> List[Dict[str, str]]:
    """Search the web for information.
    
    Args:
        query: The search query
        
    Returns:
        A list of search results
    """
    # Mock implementation
    return [
        {"title": f"Result 1 for {query}", "snippet": "This is the first search result."},
        {"title": f"Result 2 for {query}", "snippet": "This is the second search result."},
        {"title": f"Result 3 for {query}", "snippet": "This is the third search result."}
    ]


@tool
def summarize_text(text: str, max_length: int = 100) -> str:
    """Summarize a text to a specified maximum length.
    
    Args:
        text: The text to summarize
        max_length: Maximum length of the summary
        
    Returns:
        The summarized text
    """
    # In a real implementation, this would use an LLM to summarize
    # This is a mock implementation
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


class MultiAgentSystem:
    """A system with multiple specialized agents."""
    
    def __init__(self):
        """Initialize the multi-agent system with specialized agents."""
        # Research agent with web search capability
        self.research_agent = Agent(
            tools=[web_search],
            name="ResearchAgent"
        )
        
        # Summarization agent
        self.summary_agent = Agent(
            tools=[summarize_text],
            name="SummaryAgent"
        )
        
        # Coordinator agent that can delegate to other agents
        self.coordinator = Agent(
            tools=[self._delegate_to_research, self._delegate_to_summary],
            name="CoordinatorAgent"
        )
    
    @tool
    def _delegate_to_research(self, query: str) -> str:
        """Delegate a query to the research agent.
        
        Args:
            query: The research query
            
        Returns:
            The research results
        """
        return self.research_agent(f"Research this topic: {query}")
    
    @tool
    def _delegate_to_summary(self, text: str, max_length: int = 100) -> str:
        """Delegate text summarization to the summary agent.
        
        Args:
            text: The text to summarize
            max_length: Maximum length of the summary
            
        Returns:
            The summarized text
        """
        return self.summary_agent(f"Summarize this text in {max_length} characters: {text}")
    
    def process_query(self, query: str) -> str:
        """Process a user query through the multi-agent system.
        
        Args:
            query: The user's query
            
        Returns:
            The system's response
        """
        return self.coordinator(query)


def main():
    """Run the multi-agent system."""
    system = MultiAgentSystem()
    
    print("Multi-Agent System initialized.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Process the user input with the multi-agent system
        response = system.process_query(user_input)
        print(f"\nSystem: {response}")


if __name__ == "__main__":
    print("Starting Strands Multi-Agent System...")
    print("Note: This requires the strands-agents package to be installed.")
    print("Install with: pip install strands-agents")
    main()
