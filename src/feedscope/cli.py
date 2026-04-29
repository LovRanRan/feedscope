import typer

app = typer.Typer()


@app.command()
def hello() -> None:
    typer.echo("Hello world!")


if __name__ == "__main__":
    app()
