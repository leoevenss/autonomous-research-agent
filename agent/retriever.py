import arxiv

paper_cache = {}

def retrieve_papers(state):
    query = state["query"]

    if query in paper_cache:
        return {"papers": paper_cache[query]}

    papers = []

    try:
        search = arxiv.Search(query=query, max_results=3)

        for r in search.results():
            papers.append({
                "title": r.title,
                "summary": r.summary[:300],
                "url": r.entry_id
            })

    except:
        papers = [{
            "title": "Conceptual Knowledge",
            "summary": f"{query} explanation with key ideas.",
            "url": ""
        }]

    paper_cache[query] = papers
    return {"papers": papers}