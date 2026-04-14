from agent.utils import cached_llm, clean_output

def llm_compare(state, llm):
    context = "\n".join([
        f"{p['title']}: {p['summary']}"
        for p in state["papers"]
    ])

    prompt = f"""
### Instruction:
Compare the following.

### Input:
{context}

### Output:
Key Differences:
- ...

Strengths:
- ...

Weaknesses:
- ...

Use Cases:
- ...
"""

    output = cached_llm(llm, prompt)
    output = clean_output(output)

    return {"synthesis": output}


def llm_summarize(state, llm):
    context = "\n".join([
        f"{p['title']}: {p['summary']}"
        for p in state["papers"]
    ])

    prompt = f"""
Summarize clearly:

{context}
"""

    output = cached_llm(llm, prompt)
    output = clean_output(output)

    return {"synthesis": output}