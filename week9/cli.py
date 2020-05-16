import click
import logic
import rest

@click.group()
def manager():
    pass

@manager.command()
@click.option('--one', '-1', is_flag=True)
@click.option('--two', '-2')
@click.option('--three', '-3', is_flag=True)
def exercise(one,two,three):
    if(one):
        logic.ex01()
    elif(two):
        logic.ex02(two)
    elif(three):
        rest.flask_run()