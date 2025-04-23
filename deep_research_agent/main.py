import os
import sys
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent 
sys.path.insert(0, str(project_root))

from deep_research_agent.graph.graph import app

load_dotenv()

def run_graph(query: str):
    """Runs the LangGraph agent with the given query and streams results."""
    final_answer = None
    if "TAVILY_API_KEY" not in os.environ:
        yield "error", "TAVILY_API_KEY not set. Please configure it in the .env file."
        return

    inputs = {"query": query}
    yield "status", f"Starting research for: '{query}'..."
    yield "status", "Decomposing query..."

    try:
        config = {"recursion_limit": 15} 
        for output in app.stream(inputs, config=config):
            for key, value in output.items():
                yield "status", f"Running node: {key}..."
                if key == "decompose_query":
                    yield "decomposition", value.get('sub_queries', [])
                elif key == "research":
                    yield "research", value.get('research_results', [])
                elif key == "generate_draft":
                    final_answer = value.get('draft_answer', 'N/A')
                    yield "draft", final_answer 

    except Exception as e:
        yield "error", f"An error occurred during graph execution: {e}"
        return

    yield "status", "Research complete."

if __name__ == "__main__":
    test_query = "What are the latest advancements in AI-powered drug discovery?"
    print(f"Running graph via command line with query: '{test_query}'")
    print("--- Starting Graph Execution ---")

    for step_type, step_output in run_graph(test_query):
        print(f"\n[{step_type.upper()}]")
        print("---")
        if isinstance(step_output, list):
            print(f"Count: {len(step_output)}")
        else:
            print(step_output)
        print("\n---\n")

    print("--- Graph Execution Finished ---")
