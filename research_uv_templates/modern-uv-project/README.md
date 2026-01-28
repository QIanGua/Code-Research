# Modern Python Project Template

A best-practice, minimal, and complete Python project template using modern tools.

## Tools Used

- **[uv](https://github.com/astral-sh/uv)**: Extremely fast Python package installer and resolver. Manages dependencies and virtual environments.
- **[Hatchling](https://hatch.pypa.io/latest/)**: Modern, standards-compliant build backend.
- **[Ruff](https://github.com/astral-sh/ruff)**: Extremely fast Python linter and formatter. Replaces Flake8, Black, isort, etc.
- **[Pytest](https://docs.pytest.org/)**: The standard for Python testing.
- **[Mypy](https://mypy-lang.org/)**: Static type checker (configured in strict mode).
- **[Just](https://github.com/casey/just)**: A handy command runner to save and run project-specific commands.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) installed.
- [just](https://github.com/casey/just) installed (optional, but recommended).

## Usage

### Setup

Initialize the environment and install dependencies:

```bash
just setup
# Or directly:
uv sync
```

### Development

Run the test suite:

```bash
just test
# Or:
uv run pytest
```

Format code (auto-fix):

```bash
just format
# Or:
uv run ruff format . && uv run ruff check --fix .
```

Lint code (check style and types without modifying):

```bash
just lint
# Or:
uv run ruff check . && uv run ruff format --check . && uv run mypy .
```

Clean build artifacts:

```bash
just clean
```

## Project Structure

- `pyproject.toml`: Single configuration file for project metadata, dependencies, and tools.
- `Justfile`: Task runner definitions.
- `src/`: Source code directory.
- `tests/`: Test directory.
- `uv.lock`: Locked dependencies for reproducible builds.
