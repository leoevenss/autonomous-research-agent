from agent.utils import log

def router(state):
    q = state["query"].lower()

    if "compare" in q or "vs" in q:
        route = "compare"
    elif "paper" in q or "research" in q:
        route = "research"
    else:
        route = "deep_dive"

    log(state, f"Routing to {route}")
    return {"route": route}