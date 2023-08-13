# Installation

The installation relies on [Poetry](https://python-poetry.org/), once it is installed you can define your virtualenv for the project with:

```bash
poetry install
```

# Testing

Still with [Poetry](https://python-poetry.org/):

```bash
poetry run pytest
```

# Example

An exemple of fighting-fantasy book parsing (french edition of Deathtrap Dungeon)

```bash
poetry run python scripts/jouons.py
```

The file `labyrinthe.graphml` is now available to analyze with some tool like [Gephi](https://gephi.org/)

