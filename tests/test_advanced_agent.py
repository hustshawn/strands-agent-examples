"""
Tests for the advanced_agent.py module.
"""

import pytest
from advanced_agent import search_database, calculate, knowledge_lookup, knowledge_add


def test_search_database():
    """Test the search_database tool."""
    results = search_database("agent")
    assert len(results) > 0
    assert any("agent" in result["title"].lower() or "agent" in result["content"].lower() for result in results)


def test_search_database_limit():
    """Test the search_database tool with a limit."""
    results = search_database("a", limit=2)
    assert len(results) <= 2


def test_calculate():
    """Test the calculate tool."""
    result = calculate("2 + 2")
    assert result == 4.0
    
    result = calculate("10 * 5")
    assert result == 50.0


def test_knowledge_base():
    """Test the knowledge base tools."""
    # Clear any existing knowledge base
    if hasattr(knowledge_lookup, "kb"):
        delattr(knowledge_lookup, "kb")
    
    # Look up existing knowledge
    result = knowledge_lookup("strands")
    assert "model-driven" in result.lower()
    
    # Add new knowledge
    knowledge_add("test", "This is a test entry")
    
    # Look up the new knowledge
    result = knowledge_lookup("test")
    assert "test entry" in result.lower()