import matplotlib.pyplot as plt
from exercise_module import ExerciseModule


def bar_plot():
    em = ExerciseModule(None)
    # em.multi
    plt.bar(em.file_dict().keys(), sorted(em.file_dict().values()))
    plt.title("Location vs Population")
    #plt.xticks(em.file_dict().keys(), rotation='vertical', fontsize=10)
    plt.ylabel("Location")
    plt.xlabel("Population")
    plt.show()
