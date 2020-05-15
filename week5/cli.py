import click
from logic.ex01 import statsbank_format, create_csv, divorced as div, direct, never_married, marrital_status
import logic.ex01 as logic
import logic.ex02 as ex02


@click.group()
def manager():
    pass


@manager.command()
@click.option('--one', '-o', type=click.Choice(['divorced', 'nevermarried', 'marrital', 'marnev']))
@click.option('--two', '-t', type=click.Choice(['sea', 'all2018','research','finance', 'construction']))
def exercise(one, two):
    if(one):
        {
            'divorced': div,
            'nevermarried': never_married,
            'marrital': marrital_status,
            'marnev':logic.married_nevermarried
        }.get(one)()
    elif(two):
        {
            'sea':ex02.sea_employee_count,
            'all2018':ex02.all2018,
            'research':ex02.research,
            'finance':ex02.finance,
            'construction':ex02.construction
        }.get(two)()


@manager.command()
@click.argument("columns", nargs=-1)
def sync(columns):
    """
    OMRÅDE,KØN,ALDER,TID,CIVILTILSTAND
    """
    if(columns):
        create_csv(statsbank_format(columns))


@manager.command()
@click.argument("columns", nargs=-1)
def nosave(columns):
    if(columns):
        direct(columns)
