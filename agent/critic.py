def critic(state):
    text = state["synthesis"]

    if "Key Differences" in text:
        return {"critique": "Good"}
    return {"critique": "Weak structure"}