from typing import Dict, Any, List
from deep_research_agent.graph.state import GraphState

def format_results_with_citations(results: List[Dict[str, Any]]) -> str:
    if not results:
        return "No research results found."

    formatted_output = "Based on the research, here's a summary:\n\n"
    citations = []
    citation_map = {}

    for i, result in enumerate(results):
        content = result.get('content', 'N/A')
        url = result.get('url', 'N/A')
        title = result.get('title', 'Untitled')

        if url not in citation_map:
            citation_map[url] = len(citations) + 1
            citations.append(f"[{citation_map[url]}] {title} ({url})")

        citation_num = citation_map[url]
        formatted_output += f"- {content} [{citation_num}]\n"

    formatted_output += "\nSources:\n"
    formatted_output += "\n".join(citations)

    return formatted_output

def draft_answer_node(state: GraphState) -> Dict[str, Any]:
    print("---DRAFTING ANSWER NODE---")
    research_results = state.get("research_results")

    if not research_results:
        print("No research results to draft from.")
        return {"draft_answer": "Could not generate an answer as no research results were found."}

    draft = format_results_with_citations(research_results)

    print("Draft answer generated.")
    return {"draft_answer": draft}

if __name__ == '__main__':
    test_state: GraphState = {
        "query": "Test Query",
        "sub_queries": [],
        "research_results": [
            {"content": "Content from source 1 about topic A.", "url": "http://example.com/source1", "title": "Source 1 Title"},
            {"content": "More details from source 1.", "url": "http://example.com/source1", "title": "Source 1 Title"},
            {"content": "Information from source 2 regarding topic B.", "url": "http://example.com/source2", "title": "Source 2 Title"},
        ],
        "draft_answer": "",
        "error": None
    }
    draft_output = draft_answer_node(test_state)
    print("\n---Drafted Answer---")
    print(draft_output.get("draft_answer"))
