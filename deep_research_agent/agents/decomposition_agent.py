from typing import Dict, Any, List
from deep_research_agent.graph.state import GraphState

def _decompose_query_placeholder(query: str) -> List[str]:
    print(f"Decomposing query (placeholder): '{query}'")
    sub_queries = []
    if " and " in query:
        sub_queries = [q.strip() for q in query.split(" and ")]
    elif " vs " in query:
         sub_queries = [f"What is {q.strip()}?" for q in query.split(" vs ")]
         sub_queries.append(f"Comparison between {query.split(' vs ')[0].strip()} and {query.split(' vs ')[1].strip()}")
    else:
        sub_queries = [
            query,
            f"Key aspects of {query}",
            f"Recent developments in {query}"
        ]

    final_sub_queries = list(set(sub_queries))[:3]
    print(f"Generated sub-queries: {final_sub_queries}")
    return final_sub_queries


def decompose_query_node(state: GraphState) -> Dict[str, Any]:
    print("---DECOMPOSE QUERY NODE---")
    query = state["query"]
    sub_queries = _decompose_query_placeholder(query)
    return {"sub_queries": sub_queries}

if __name__ == '__main__':
    test_state: GraphState = {
        "query": "Latest advancements in AI-powered drug discovery and clinical trials",
        "sub_queries": [],
        "research_results": [],
        "draft_answer": "",
        "error": None
    }
    decomposition_output = decompose_query_node(test_state)
    print("\n---Decomposition Output---")
    print(decomposition_output)

    test_state_2: GraphState = {
        "query": "LangGraph vs AutoGen",
         "sub_queries": [], "research_results": [], "draft_answer": "", "error": None
    }
    decomposition_output_2 = decompose_query_node(test_state_2)
    print("\n---Decomposition Output 2---")
    print(decomposition_output_2)
