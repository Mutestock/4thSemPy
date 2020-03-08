import click
from exercise_module import ExerciseModule


@click.group()
def manager():
    pass


@manager.command()
@click.option('--download', '-d', nargs=2)
@click.option('--avg', '-a')
@click.option('..hread', 'h', is_flag=True)
def command(download, avg, hread):
    if(download):
        ExerciseModule.download(download[0], download[1])
    elif(avg):
        ExerciseModule.avg_vowels(avg)
    elif(hread):
        ExerciseModule.hard_read()


@manager.command()
@click.argument('urls', nargs=-1)
def multi(urls):
    if(urls):
        em = ExerciseModule(None)
        em.multi_download(list(urls))
        em.hardest_read()
