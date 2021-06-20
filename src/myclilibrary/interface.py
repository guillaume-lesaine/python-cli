import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", help="Name of the database", required=True)
def initdb(name: str) -> None:
    """Initialize a database."""

    if name == "oops":
        raise ValueError("Value 'oops' is forbidden for option '--name'.")

    click.echo(f"Initialized the database '{name}'")
