import click
import logic

@click.group()
def manager():
    pass


@manager.command()
@click.option('--ex', '-e', type=click.Choice(['1','2','3','4','5','6']))
def exercise(ex):
    if(ex):
        {
            '1':logic.load_csv,
            '2':logic.unique_labels,
            '3':logic.scatter01,
            '4':logic.cluster,
            '5':logic.cluster_print,
            '6':logic.scatter02
        }.get(ex)()