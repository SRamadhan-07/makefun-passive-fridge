"""Write the passive-aggressive fridge note to /output/entry.txt."""

from pathlib import Path

NOTE = (
    "Opened fourteen times today. Nothing taken. "
    "I, too, enjoy being looked at like an answer."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_note(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    write_note(OUTPUT_PATH, NOTE)


if __name__ == "__main__":
    main()
