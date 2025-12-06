from src.agents.llm_client import LLMClient

class StaticAnalysisAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, code: str) -> str:
        prompt = (
            "Perform static code analysis on the following code. "
            "Identify syntax issues, bad practices, or logical problems.\n\n"
            f"{code}"
        )
        return self.llm.chat(prompt)
