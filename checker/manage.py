import click

from flask.cli import FlaskGroup

from checker.app import create_app


def create_checker(info):
    return create_app()


@click.group(cls=FlaskGroup, create_app=create_checker)
def cli():
    """Main entry point"""
    pass


if __name__ == "__main__":
    cli()
