import os
from tavily import TavilyClient
from typing import List, Dict, Any
from deep_research_agent.graph.state import GraphState

def research_node(state: GraphState) -> Dict[str, Any]:
    print("---RESEARCH NODE---")

    try:
        tavily_api_key = os.environ["TAVILY_API_KEY"]
        tavily_client = TavilyClient(api_key=tavily_api_key)
    except KeyError:
        print("Error: TAVILY_API_KEY environment variable not set or found.")
        return {"error": "TAVILY_API_KEY not configured."}

    query = state["query"]
    sub_queries = state.get("sub_queries", [query])

    all_results: List[Dict[str, Any]] = []

    print(f"Researching sub-queries: {sub_queries}")

    for sub_query in sub_queries:
        try:
            response = tavily_client.search(
                query=sub_query,
                search_depth="advanced",
                max_results=5
            )

            if 'results' in response:
                for result in response['results']:
                    all_results.append({
                        "query": sub_query,
                        "content": result.get('content', ''),
                        "url": result.get('url', ''),
                        "title": result.get('title', ''),
                    })
            print(f"Found {len(response.get('results', []))} results for '{sub_query}'")

        except Exception as e:
            print(f"Error during Tavily search for '{sub_query}': {e}")

    print(f"Total research results collected: {len(all_results)}")
    return {"research_results": all_results}

if __name__ == '__main__':
    print("Direct execution of research_agent.py for testing is currently disabled.")
