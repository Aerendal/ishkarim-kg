"""
ishkarim_kg — moduł z obszaru kg.

Grafy wiedzy: GraphRAG, LinkML, SHACL, ontologie, RDF w SQLite.

Źródła: 14 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "kg"



MODULES: list[str] = [
    'Algorytm Pearla w AI',
    'AutoSchemaKG - ShapeSpresso - LinkML - Metanome',
    'Automatyczne schematy i hybrydowe wyszukiwanie w Qdrant',
    'Graph‑RAG, NLIs & Visual Builders',
    'Indukcja schematów JSON-Schema i SHACL',
    'Indukcja schematów i ontologii wykonawczych',
    'LinkML w pre-commit i Actions  - walidacja offline',
    'Lokalne grafy semantyczne i silniki narracyjne',
    'MVP Fraktalnego Słownika',
    'Mapa klastrów i ich punkty obserwacji',
    'New methods for KG consistency  and coverage',
    'Semantic IR i ścieżka kompilacji CPU‑only',
    'Zestawy OSS do ewaluacji RAG i KG (2025–26)',
    'Śledzenie wymagań i pokrycia w Doorstop-shell tracer',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "kg"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
