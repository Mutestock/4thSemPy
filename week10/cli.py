import click
import logic

@click.group()
def manager():
    pass


@manager.command()
#@click.option('--ex', '-e', type=click.Choice([]))
def exercise():
    print(logic.unique_labels())