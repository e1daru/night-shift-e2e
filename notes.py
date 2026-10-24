from pathlib import Path


def load_notes(folder: str) -> str:
    return "\n\n".join(f"## {p.name}\n{p.read_text()}" for p in sorted(Path(folder).glob("*.md")))
