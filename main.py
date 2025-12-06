from src.agents.static_analysis_agent import StaticAnalysisAgent
from src.agents.bug_finder_agent import BugFinderAgent
from src.agents.improvement_agent import ImprovementAgent
from src.agents.documentation_agent import DocumentationAgent

if __name__ == "__main__":
    print("Paste your code below (end with CTRL+D / CTRL+Z):\n")
    
    try:
        code = ""
        while True:
            code += input() + "\n"
    except EOFError:
        pass

    static_agent = StaticAnalysisAgent()
    bug_agent = BugFinderAgent()
    improve_agent = ImprovementAgent()
    doc_agent = DocumentationAgent()

    static_res = static_agent.run(code)
    bug_res = bug_agent.run(code)
    improve_res = improve_agent.run(code)
    doc_res = doc_agent.run(code)

    print("\n=== AI CODE REVIEW REPORT ===\n")
    print("STATIC ANALYSIS:\n", static_res)
    print("\nBUG FINDINGS:\n", bug_res)
    print("\nSUGGESTED IMPROVEMENTS:\n", improve_res)
    print("\nGENERATED DOCUMENTATION:\n", doc_res)
