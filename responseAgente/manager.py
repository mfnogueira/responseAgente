from responseagent.agente import Agent
from responseagent.reviews_intelligence_agent import ReviewsIntelligenceAgent
from responseagent.estatistica_agent import EstatisticaAgent
from responseagent.storytelling_agent import StorytellingAgent

class Manager:
    def __init__(self):
        self.agents = {
            "reviews_intelligence": ReviewsIntelligenceAgent(),
            "estatistica": EstatisticaAgent(),
            "storytelling": StorytellingAgent()
        }

    def handle_request(self, request_type, data):
        if request_type not in self.agents:
            raise ValueError(f"No agent found for request type: {request_type}")
        return self.agents[request_type].process(data)
