import click
from logic import reg_log_file, rip_info


@click.group()
def manager():
    pass


@manager.command()
@click.option("--regfile", "-r")
@click.option("--htmlrip", "-h")
def ex(regfile, htmlrip):
    if regfile:
        print(reg_log_file(regfile))
    if htmlrip:
        rip_info(htmlrip)

