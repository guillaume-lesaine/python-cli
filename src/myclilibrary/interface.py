import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--count", help="number of greetings", required=True)
def initdb(count: str) -> None:
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"Initialized the database '{count}'")


@cli.command()
def dropdb():
    click.echo("Dropped the database")
