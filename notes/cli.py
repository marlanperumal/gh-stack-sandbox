import sys
from pathlib import Path

from notes.models import Note
from notes.storage import load, save


def main() -> None:
    path = Path("notes.json")
    notes = load(path) if path.exists() else []
    notes.append(Note(id=len(notes) + 1, title=sys.argv[1], body=sys.argv[2]))
    save(notes, path)


if __name__ == "__main__":
    main()
