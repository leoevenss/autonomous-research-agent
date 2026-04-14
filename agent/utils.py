llm_cache = {}

def cached_llm(llm, prompt):
    if prompt in llm_cache:
        return llm_cache[prompt]

    output = llm(prompt)

    if isinstance(output, list):
        output = output[0]["generated_text"]

    llm_cache[prompt] = output
    return output


def clean_output(text):
    if not isinstance(text, str):
        text = str(text)

    lines = text.split("\n")
    cleaned = []

    for i, line in enumerate(lines):
        if line.strip().startswith("##") and (i+1 >= len(lines) or lines[i+1].strip() == ""):
            continue
        cleaned.append(line)

    return "\n".join(cleaned)


def log(state, message):
    if "logs" not in state:
        state["logs"] = []
    state["logs"].append(message)