from src.agents.llm_client import LLMClient

class DocumentationAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, code: str) -> str:
        prompt = (
            "Generate clear docstrings and inline comments for this code. "
            "Follow best documentation practices.\n\n"
            f"{code}"
        )
        return self.llm.chat(prompt)
