import json
with open("/home/mira/.claude/projects/-home-mira--session-461166735379/2c07aae1-f058-4571-b730-f2f4bcd011a0/tool-results/call_57396d33015140af94c665158debd9b6.json") as f:
    data = json.load(f)
for idx, res in enumerate(data[0]["data"]["batch_results"]):
    for item in res["context_datas"]:
        w = item["web_search_result"]
        title = w.get("title")
        url = w.get("url")
        content = w.get("content")[:500] if w.get("content") else ""
        print(f"[{idx}] {title}
URL: {url}
Content: {content}
" + "-"*50)
