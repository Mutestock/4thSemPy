import click
from logic import csv_to_numpy_ndarray, find_ppl_per_dict, bar_small_to_large, bool_mask, bool_mask_99, line_plot_01
from data import dk_data, neighb
import os


@click.group()
def manager():
    pass


@manager.command()
@click.option("--exercise",
              "-e",
              type=click.Choice(["2", "3", '4', '5', '6', '7'],
                                case_sensitive=False))
@click.option("--datasync",
              "-d",
              type=click.Choice(["2"], case_sensitive=False))
def assignment(exercise, datasync):
    if (exercise is '2'):
        for line in csv_to_numpy_ndarray(dk_data)[:30]:
            print(line)
        print("...etc")
    elif (exercise is '3'):
        for key, val in find_ppl_per_dict(neighb, dk_data).items():
            print("Location: " + key + " | Population: " + str(val))
    elif (exercise is '4'):
        bar_small_to_large()
    elif (exercise is '5'):
        print("Population 65 yr old, yr 2015: " + str(bool_mask()))
    elif (exercise is '6'):
        print("Population 65 yr old, yr 2015, code 99: " + str(bool_mask_99()))
    elif (exercise is '7'):
        line_plot_01()