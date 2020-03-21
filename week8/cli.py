import click
import logic


@click.group()
def manager():
    pass


@manager.command()
@click.option("--command", "-c", type=click.Choice(["01"]))
def ex(command):
    if command:
        pseudo_switch = {"01": logic.data_sync}
        pseudo_switch.get(command)()

