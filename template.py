import os

folders = [
    "src",
    "src/agents",
    "src/api"
]

files = {
    "main.py": "",
    "requirements.txt": "",
    "Dockerfile": "",
    "src/__init__.py": "",
    "src/agents/__init__.py": "",
    "src/api/__init__.py": "",
    "src/agents/llm_client.py": "",
    "src/agents/static_analysis_agent.py": "",
    "src/agents/bug_finder_agent.py": "",
    "src/agents/improvement_agent.py": "",
    "src/agents/documentation_agent.py": "",
    "src/api/server.py": "",
}

print("\n📁 Creating AI Code Review Agent structure...\n")

for f in folders:
    os.makedirs(f, exist_ok=True)
    print(f"Created folder: {f}")

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Created file: {path}")

print("\n✅ Structure created successfully!")
