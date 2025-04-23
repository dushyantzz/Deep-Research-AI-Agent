import os
from langgraph.graph import StateGraph, END
from deep_research_agent.graph.state import GraphState
from deep_research_agent.agents.research_agent import research_node
from deep_research_agent.agents.drafting_agent import draft_answer_node
from deep_research_agent.agents.decomposition_agent import decompose_query_node

workflow = StateGraph(GraphState)

workflow.add_node("decompose_query", decompose_query_node)
workflow.add_node("research", research_node)
workflow.add_node("generate_draft", draft_answer_node)

workflow.set_entry_point("decompose_query")
workflow.add_edge("decompose_query", "research")
workflow.add_edge("research", "generate_draft")
workflow.add_edge("generate_draft", END)

app = workflow.compile()
