# Personal Knowledge Router

A local Python CLI that assigns notes to categories using transparent keyword rules.

## Usage

```bash
python router.py examples/notes.json
python -m unittest discover -s tests -v
```

Input is a JSON object with `notes` (objects containing `id` and `text`) and `rules` (category-to-keyword mapping). Each note is assigned the category with the highest keyword occurrence count; ties use rule insertion order. Unmatched notes are marked `uncategorized`.

No network calls or cloud storage. This is **keyword routing**, not semantic search, encryption, or an AI-powered knowledge base. Avoid storing sensitive notes without appropriate local file protection.
