import click
import logic

@click.group()
def manager():
    pass


@manager.command()
@click.option('--ex', '-e', type=click.Choice(['1','2','3','4','5','6','7','8']))
def exercise(ex):
    if(ex):
        {
            '1':logic.load_csv,
            '2':logic.unique_labels,
            '3':logic.scatter01,
            '4':logic.cluster_print
        }.get(ex)()