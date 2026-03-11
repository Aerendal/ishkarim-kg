#!/usr/bin/env python3
"""
demo.py — demo ishkarim-kg

Grafy wiedzy lokalnie — GraphRAG, LinkML, SHACL walidacja, ontologie w SQLite

Uruchomienie:
    python projects/ishkarim-kg/demo.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_kg as m

docs = m.load_knowledge_index()
linkml_docs = [d for d in docs if "linkml" in d["name"].lower() or "ontolog" in d["name"].lower()]
shacl_docs  = [d for d in docs if "shacl" in d["name"].lower() or "schema" in d["name"].lower()]
graph_docs  = [d for d in docs if "graph" in d["name"].lower()]

print(f"Grafy wiedzy — {len(docs)} katalogów wiedzy")
print(f"  LinkML/Ontologie: {len(linkml_docs)}")
print(f"  SHACL/Schema:     {len(shacl_docs)}")
print(f"  GraphRAG:         {len(graph_docs)}")
print()
for d in docs[:4]:
    print(f"  [{d['maturity']:8s}] {d['name'][:65]}")

