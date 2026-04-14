memory_store = {
    "chat_history": [],
    "research_notes": []
}

def update_memory(state):
    if len(state.get("synthesis", "")) < 50:
        return {}

    memory_store["chat_history"].append(state["query"])
    memory_store["research_notes"].append(state["synthesis"][:200])

    return {}