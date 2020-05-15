import click


def manager():
    pass


@manager.command()
@click.option('--one','-o' type=click.Choice([])
def exercise(one):
	if(one):
		{
		
		}.get(one)()