"""
extracted.py — kod wyekstrahowany z WORK.md dla obszaru kg.

Zawiera 3 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: AutoSchemaKG - ShapeSpresso - LinkML - Metanome
@dataclass(frozen=True)
class SlotSig:
    range: str; required: bool; identifier: bool; multivalued: bool
# Klucz diff: (class_name, slot_name) → old_sig vs new_sig
# identifier=True → zmiana jest zawsze breaking/risky
# unique_keys: dodanie → risky; usunięcie → breaking

# Source: Automatyczne schematy i hybrydowe wyszukiwanie w Qdrant
from qdrant_client import QdrantClient, models
client = QdrantClient(url="http://localhost:6333")
client.create_collection(
    collection_name="kb_chunks_v1",
    vectors_config={
        "dense":   models.VectorParams(size=384, distance=models.Distance.COSINE),
        "colbert": models.VectorParams(size=128, distance=models.Distance.COSINE),
    },
    sparse_vectors_config={"sparse": models.SparseVectorParams()},
)

# Source: Indukcja schematów JSON-Schema i SHACL
CONFIG = {
  "required_threshold": 0.98,
  "null_threshold": 0.05,
  "min_samples_enum": 100,
  "max_unique_enum": 20,
  "enum_stability_ratio": 0.1,
  "unique_cap": 500,
}
