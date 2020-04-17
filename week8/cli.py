import click
import logic
from rest import flask_run


@click.group()
def manager():
    pass


@manager.command()
@click.option("--sync", "-s", is_flag=True)
@click.option("--between", "-b", nargs=2)
@click.option("--flask", "-f", is_flag=True)
def ex(sync, between, flask):
    if sync:
        logic.data_sync()
    elif between:
        logic.crimes_between_dates(between[0], between[1])
    elif flask:
        flask_run()

