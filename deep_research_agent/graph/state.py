from typing import List, TypedDict, Optional, Dict, Any

class GraphState(TypedDict):
    query: str
    sub_queries: List[str]
    research_results: List[Dict[str, Any]]
    draft_answer: str
    error: Optional[str]
