from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    query: str
    route: str
    papers: List[Dict]
    notes: List[str]
    synthesis: str
    critique: str
    logs: List[str]