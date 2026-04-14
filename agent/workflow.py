from langgraph.graph import StateGraph, END

from agent.router import router
from agent.retriever import retrieve_papers
from agent.nodes import llm_compare, llm_summarize
from agent.critic import critic
from agent.memory import update_memory


def build_workflow(llm):

    workflow = StateGraph(dict)

    workflow.add_node("router", router)
    workflow.add_node("retrieve", retrieve_papers)

    workflow.add_node("compare", lambda s: llm_compare(s, llm))
    workflow.add_node("summarize", lambda s: llm_summarize(s, llm))

    workflow.add_node("critic", critic)
    workflow.add_node("memory", update_memory)

    workflow.set_entry_point("router")

    workflow.add_edge("router", "retrieve")

    workflow.add_conditional_edges(
        "retrieve",
        lambda s: s["route"],
        {
            "compare": "compare",
            "research": "summarize",
            "deep_dive": "summarize"
        }
    )

    workflow.add_edge("compare", "critic")
    workflow.add_edge("summarize", "critic")

    workflow.add_edge("critic", "memory")
    workflow.add_edge("memory", END)

    return workflow.compile()