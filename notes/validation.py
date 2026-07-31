from notes.models import Note


def validate(note: Note) -> None:
    if not note.title:
        raise ValueError("title required")
