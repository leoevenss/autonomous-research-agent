import gradio as gr
from agent.llm import load_llm
from agent.workflow import build_workflow

llm = load_llm()
app = build_workflow(llm)

def run_agent(query):
    result = app.invoke({
        "query": query,
        "route": "",
        "papers": [],
        "notes": [],
        "synthesis": "",
        "critique": "",
        "logs": []
    })

    return f"""
### 🧠 Output
{result.get("synthesis","")}

---

### 🔍 Critique
{result.get("critique","")}
"""

ui = gr.Interface(
    fn=run_agent,
    inputs=gr.Textbox(lines=2, placeholder="Ask something..."),
    outputs="markdown",
    title="Autonomous Research Agent"
)

if __name__ == "__main__":
    ui.launch()