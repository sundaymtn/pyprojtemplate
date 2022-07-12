"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Project Template."""


if __name__ == "__main__":
    main(prog_name="pyprojtemplate")  # pragma: no cover
