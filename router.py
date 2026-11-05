"""Route text notes into user-defined categories with keyword scores."""
import argparse
import json
import sys

def route(notes,rules):
    if not isinstance(notes,list) or not isinstance(rules,dict): raise ValueError("notes must be a list and rules an object")
    if any(not isinstance(name,str) or not isinstance(words,list) or any(not isinstance(w,str) or not w for w in words) for name,words in rules.items()):
        raise ValueError("rules must map categories to keyword arrays")
    results=[]
    for i,note in enumerate(notes):
        if not isinstance(note,dict) or not isinstance(note.get("text"),str):
            raise ValueError("invalid note at index "+str(i))
        text=note["text"].casefold()
        scores={name:sum(text.count(word.casefold()) for word in words) for name,words in rules.items()}
        best=max(scores,key=lambda name:scores[name]) if scores else None
        category=best if best is not None and scores[best]>0 else "uncategorized"
        results.append({"id":note.get("id",i),"category":category,"score":scores.get(category,0)})
    return {"total":len(results),"routes":results}

def main(argv=None):
    p=argparse.ArgumentParser(description="Route notes by keyword")
    p.add_argument("file")
    args=p.parse_args(argv)
    try:
        with open(args.file,encoding="utf-8") as f: data=json.load(f)
        if not isinstance(data,dict): raise ValueError("input must be an object")
        result=route(data.get("notes"),data.get("rules"))
    except (OSError,ValueError,TypeError) as exc:
        print(str(exc),file=sys.stderr)
        return 2
    print(json.dumps(result,indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
