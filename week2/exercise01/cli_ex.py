import click
from file_logic import print_file_content, write_list_to_file, read_csv, urlList
from file_logic import download as dl


@click.group()
def manager():
    pass


@manager.command()
@click.option("-f", '--file', help="will write to a file instead of reading it")
@click.option("-p", "--path", required=True, help="describes the file you want to interact with")
@click.option("-d", "--download", flag_value=True, help="inserts some testdata in a separate download file")
def files(path, file, download):
    if(download):
        dl(urlList)
    if(file):
        write_list_to_file(file, read_csv(path))
    else:
        print_file_content(path)
