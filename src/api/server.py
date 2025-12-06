from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.static_analysis_agent import StaticAnalysisAgent
from src.agents.bug_finder_agent import BugFinderAgent
from src.agents.improvement_agent import ImprovementAgent
from src.agents.documentation_agent import DocumentationAgent

app = FastAPI(title="AI Code Review Agent API")

static_agent = StaticAnalysisAgent()
bug_agent = BugFinderAgent()
improve_agent = ImprovementAgent()
doc_agent = DocumentationAgent()

class CodeRequest(BaseModel):
    code: str

@app.post("/review")
async def review_code(req: CodeRequest):
    code = req.code
    
    return {
        "static_analysis": static_agent.run(code),
        "bug_analysis": bug_agent.run(code),
        "improvements": improve_agent.run(code),
        "documentation": doc_agent.run(code)
    }
