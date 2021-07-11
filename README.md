[![myclilibrary](https://github.com/guillaume-lesaine/python-cli/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/guillaume-lesaine/python-cli/actions/workflows/continuous-integration.yml)

# python-cli

This is a template for Python CLI library. Setting up the project for development should be as simple as:

1. Create a virtualenv: `python -m venv env`
2. Install Poetry using [official documentation](https://python-poetry.org/).
3. Install project `poetry install`
4. Setup pre-commit `poetry run pre-commit install`

The library implements a command line interface based on [click](https://palletsprojects.com/p/click/).

```bash
python -m myclilibrary --help
Usage: python -m myclilibrary [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  initdb  Initialize a database.
```