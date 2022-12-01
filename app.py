import typer

cli = typer.Typer()


@cli.command()
def nasa_api():
    with open("nasa_api_key.txt", "r") as f:
        api_key = f.read()


if __name__ == "__main__":
    cli()
