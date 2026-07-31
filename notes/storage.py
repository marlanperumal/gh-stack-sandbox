import json
from pathlib import Path

from notes.models import Note


def save(notes: list[Note], path: Path) -> None:
    path.write_text(json.dumps([n.__dict__ for n in notes]))


def load(path: Path) -> list[Note]:
    return [Note(**d) for d in json.loads(path.read_text())]
