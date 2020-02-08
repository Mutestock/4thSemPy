import click
import exercise_logic as exeLogic


@click.group()
def manager():
    pass


@manager.command()
@click.option("-p", "--path", required=True, help="The path in which all filenames will be read from")
def first(path):
    exeLogic.first_func(path)


@manager.command()
@click.option("-p", "--path", required=True, help="The path in which all filenames in the current folder and subdirectories will be read from")
def second(path):
    exeLogic.second_func(path)


@manager.command()
@click.argument("args", nargs=-1)
@click.option("--list", "-l", required=True, is_flag=True,  help="pass in list of file names")
def third(list, args):
    """
    Insert description third here
    """
    exeLogic.third_func(args)


@manager.command()
@click.argument("args", nargs=-1)
@click.option("--list", "-l", required=True, is_flag=True, help="Print all lines that starts with '@' in all filenames in the list")
def fourth(list, args):
    exeLogic.fourth_func(args)


@manager.command()
@click.argument("args", nargs=-1)
@click.option("--list", "-l", is_flag=True, required=True, help="Takes a list in which all headlines in all files will be printed to a file")
def fifth(list, args):
    exeLogic.fifth_func(args)
