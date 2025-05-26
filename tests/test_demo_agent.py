"""
Tests for the demo_agent.py module.
"""

import pytest
from demo_agent import weather_forecast, todo_list


def test_weather_forecast():
    """Test the weather_forecast tool."""
    result = weather_forecast("Seattle")
    assert result["city"] == "Seattle"
    assert len(result["forecast"]) == 3
    assert "humidity" in result
    assert "wind" in result


def test_weather_forecast_custom_days():
    """Test the weather_forecast tool with custom days."""
    result = weather_forecast("Seattle", days=1)
    assert result["city"] == "Seattle"
    assert len(result["forecast"]) == 1


def test_todo_list():
    """Test the todo_list tool."""
    # Clear the list first
    todo_list("clear")
    
    # Add items
    result = todo_list("add", "Buy milk")
    assert "Buy milk" in result
    
    result = todo_list("add", "Walk the dog")
    assert "Buy milk" in result
    assert "Walk the dog" in result
    
    # List items
    result = todo_list("list")
    assert len(result) == 2
    
    # Clear items
    result = todo_list("clear")
    assert len(result) == 0