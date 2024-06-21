from response_agent.agente import Agent
import openai

class StorytellingAgent(Agent):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def process(self, data):
        # Use OpenAI GPT to create a report from the data
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Create a detailed report based on the following data: {data}",
            max_tokens=500
        )
        report = response.choices[0].text.strip()
        return {"report": report}
