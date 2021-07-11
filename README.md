[![myclilibrary](https://github.com/guillaume-lesaine/python-cli/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/guillaume-lesaine/python-cli/actions/workflows/continuous-integration.yml)

# python-cli

This repository is a template for a Python CLI library. Setting up the project for development should be as simple as:

1. Update references to `myclilibrary` with custom name, be careful updating the folder `src/myclilibrary`.
2. Create a virtualenv with `python -m venv env`.
3. Move the virtualenv `source env/bin/activate`.
4. Install Poetry using [official documentation](https://python-poetry.org/).
5. Install project with `poetry install`.
6. Setup pre-commit with `poetry run pre-commit install`.

The library implements a command line interface based on [click](https://palletsprojects.com/p/click/) that can easily be called once installed.

```bash
python -m myclilibrary --help
Usage: python -m myclilibrary [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  initdb  Initialize a database.
```