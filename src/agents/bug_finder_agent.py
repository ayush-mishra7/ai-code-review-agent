from src.agents.llm_client import LLMClient

class BugFinderAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, code: str) -> str:
        prompt = (
            "Identify possible bugs, vulnerabilities, security issues, "
            "and edge-case failures in this code:\n\n"
            f"{code}"
        )
        return self.llm.chat(prompt)
