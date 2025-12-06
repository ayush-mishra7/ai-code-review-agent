from src.agents.llm_client import LLMClient

class ImprovementAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, code: str) -> str:
        prompt = (
            "Suggest improvements for readability, performance, and maintainability "
            "for the following code. Provide improved code if possible.\n\n"
            f"{code}"
        )
        return self.llm.chat(prompt)
