# ishkarim-kg

> **Grafy wiedzy lokalnie — GraphRAG, LinkML, SHACL walidacja, ontologie w SQLite**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Strukturalne zapytania nad bazą wiedzy (relacje, nie tylko full-text)
- Walidacja spójności ontologii przez SHACL shapes przed ingestem
- LinkML jako jeden schemat → JSON-Schema + SQL + SHACL automatycznie

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-kg

# Demo (10 sekund)
python projects/ishkarim-kg/demo.py
```

## Użycie w kodzie

```python
import ishkarim_kg as m

# Wszystkie 14 katalogi wiedzy obszaru 'kg'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_kg.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Firmowa baza wiedzy z relacjami między pojęciami i bytem
- Walidacja danych przed importem do systemu RAG
- Knowledge engineering — budowa ontologii dziedzinowej (medyczna, prawna)

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 14 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_kg.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_kg_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_kg.py --quick
```

## Struktura projektu

```
ishkarim-kg/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 14 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_kg/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_kg.py         ← testy jednostkowe
│   └── test_kg_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_kg.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 14 katalogów wiedzy obszaru `kg`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
