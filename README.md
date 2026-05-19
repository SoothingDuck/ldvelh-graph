# Installation

The installation relies on [uv](https://docs.astral.sh/uv/), once it is installed you can define your virtualenv for the project with:

```bash
uv sync
```

# Testing

Still with [uv](https://docs.astral.sh/uv/):

```bash
uv run pytest
```

# Example

An exemple of fighting-fantasy book parsing (french edition of Deathtrap Dungeon)

```bash
uv run python scripts/jouons.py
```

The file `labyrinthe.graphml` is now available to analyze with some tool like [Gephi](https://gephi.org/)
