from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search",
    model="gemini-2.0-flash",
    description="Você é um agente buscador do google.",
    instruction="""
Você é um agente que usa a ferramenta do google para buscar informações importantes para o usuário usando a tool:
- google_search
""",
    tools=[google_search],
)