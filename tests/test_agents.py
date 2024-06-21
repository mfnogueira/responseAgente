import pytest
from response_agent.reviews_intelligence_agent import ReviewsIntelligenceAgent
from response_agent.estatistica_agent import EstatisticaAgent
from response_agent.storytelling_agent import StorytellingAgent

def test_reviews_intelligence_agent():
    agent = ReviewsIntelligenceAgent()
    data = "Sample review data"
    result = agent.process(data)
    assert "insights" in result

def test_estatistica_agent():
    agent = EstatisticaAgent()
    data = {"sample": "data"}
    result = agent.process(data)
    assert "metrics" in result

def test_storytelling_agent(mocker):
    agent = StorytellingAgent()
    data = {"metrics": "sample metrics"}
    
    mock_response = mocker.Mock()
    mock_response.choices = [mocker.Mock(text="Generated report")]
    
    mocker.patch('openai.Completion.create', return_value=mock_response)
    
    result = agent.process(data)
    assert "report" in result
