import click
from exercise_module import ExerciseModule
from plot import bar_plot


@click.group()
def manager():
    pass


@manager.command()
@click.option('--download', '-d', nargs=2)
@click.option('--avg', '-a')
@click.option('--plot', '-p', type=click.Choice(['bar01'], case_sensitive=False))
def command(download, avg, plot):
    if(download):
        ExerciseModule.download(download[0], download[1])
    elif(avg):
        ExerciseModule.avg_vowels(avg)
    elif(plot):
        bar_plot()


@manager.command()
@click.argument('urls', nargs=-1)
def multi(urls):
    if(urls):
        em = ExerciseModule(None)
        em.multi_download(list(urls))
        print(em.hardest_read())
