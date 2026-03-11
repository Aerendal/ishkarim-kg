# PROBLEMS — ishkarim-kg

> Grafy wiedzy lokalnie — GraphRAG, LinkML, SHACL walidacja, ontologie w SQLite

## ✅ Co ten projekt rozwiązuje

- ✅ Strukturalne zapytania nad bazą wiedzy (relacje, nie tylko full-text)
- ✅ Walidacja spójności ontologii przez SHACL shapes przed ingestem
- ✅ LinkML jako jeden schemat → JSON-Schema + SQL + SHACL automatycznie
- ✅ GraphRAG — uzupełnienie FTS5 o relacyjne powiązania między dokumentami
- ✅ Lokalny Cypher/SPARQL bez zewnętrznego serwera (SQLite backend)

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Skalowanie do miliardów trójek RDF — lokalne, < 1M nodes
- ❌ Real-time knowledge graph updates ze strumieniowych źródeł
- ❌ Automatyczne wykrywanie relacji z tekstu — wymaga NLP pipeline
- ❌ Federated queries między wieloma grafami

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **GraphQLite Cypher support** jest eksperymentalny — nie wszystkie kwerendy działają
- ⚠️ **LinkML schema evolution** wymaga ręcznych migracji SQLite przy zmianie schematu
- ⚠️ **pyshacl** jest wolna na dużych grafach (>100k trójek) — brak parallel validation
- ⚠️ **Brak GUI** dla eksploracji grafu — tylko CLI/YASGUI

---

## 🎯 Przypadki użycia

- 🎯 Firmowa baza wiedzy z relacjami między pojęciami i bytem
- 🎯 Walidacja danych przed importem do systemu RAG
- 🎯 Knowledge engineering — budowa ontologii dziedzinowej (medyczna, prawna)
- 🎯 Uzupełnienie embeddings search o structural reasoning

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
