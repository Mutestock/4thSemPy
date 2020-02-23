import numpy as np
import os
import requests as req
import shutil
import matplotlib.pyplot as plt
from data import dk_data, neighb


def csv_to_numpy_ndarray(resource):
    """
    Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    """
    return np.genfromtxt(resource, delimiter=',', dtype=np.uint, skip_header=1)


def find_ppl_per_dict(dictionary, resource):
    """
    (...)Find out how many people lived in each of the 11 areas in 2015
    """
    data = csv_to_numpy_ndarray(resource)
    loc_pop = {}
    for element, val in dictionary.items():
        thing = data[(data[:, 1] == element) & (data[:, 0] == 2015)]
        sum_thing = thing[:, 4].sum()
        loc_pop[val] = sum_thing
    return loc_pop


def bar_small_to_large():
    '''
    Make a bar plot to show the size of each city area from the smallest to the largest
    '''
    # I am going to assume that 'smallest to largest' refers to the population
    # Bringing all of these variables in is beginning to feel very unnecessary..
    loc_pop = find_ppl_per_dict(neighb, dk_data)

    plt.bar(loc_pop.keys(), sorted(loc_pop.values()))
    plt.title("Location vs Population")
    plt.xticks(list(loc_pop.keys()), rotation='vertical', fontsize=10)
    plt.ylabel("Location")
    plt.xlabel("Population")
    plt.show()


def bool_mask():
    """
    Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
    """
    data = csv_to_numpy_ndarray(dk_data)
    mask = ((data[:, 2] > 65) & (data[:, 0] == 2015))
    return data[mask][:, 4].sum()


def bool_mask_99():
    """
    How many of those were from the other nordic countries(not dk)
    """
    data = csv_to_numpy_ndarray(dk_data)
    mask = ((data[:, 2] > 65) & (data[:, 0] == 2015) & (data[:, 1] == 99))
    return data[mask][:, 4].sum()


def line_plot_01():
    """
    Make a line plot showing the changes of number of people in versterbro and østerbro from 1992 to 2015
    """
    data = csv_to_numpy_ndarray(dk_data)
    yr_cut = data[(data[:, 0] >= 1992) & (data[:, 0] <= 2015)]

    oest_cut = data[(data[:, 1] == 2)]
    oest_uniques = np.unique(oest_cut[:, 0])
    oest_cut_finish = {}
    for item in oest_uniques:
        ee = oest_cut[(oest_cut[:, 0] == item)]
        oest_cut_finish[item] = ee[:, 4].sum()

    vest_cut = data[(data[:, 1] == 4)]
    vest_uniques = np.unique(vest_cut[:, 0])
    vest_cut_finish = {}
    for item in vest_uniques:
        ee = vest_cut[(vest_cut[:, 0] == item)]
        vest_cut_finish[item] = ee[:, 4].sum()

    plt.plot(list(oest_cut_finish.keys()), list(oest_cut_finish.values()),
             'bx')
    plt.plot(list(vest_cut_finish.keys()), list(vest_cut_finish.values()),
             'ro')
    plt.xlim(1992, 2015)
    plt.title('Vest vs oest')
    plt.show()