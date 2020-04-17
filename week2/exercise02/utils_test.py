
import os
import exercise_logic as exeLogic

if __name__ == "__main__":
    exeLogic.first_func(os.path.dirname(os.path.realpath(__file__)))
    exeLogic.second_func(os.path.dirname(os.path.realpath(__file__)))

    # I could step back in the repos and make it test stuff automatically, but I don't know what's on the user's computer and therefore I don't want to mess around with it too much
    # Additionally, I don't want to show people anything about my directories
    # and finally anyone else pulling the program and trying to run it wouldn't be able to test it, since they don't have the same directories as I do
    # Hence the list is empty
    # Here's an example of what an input variable could look like
    # "C:/Users/JohnDoe/Desktop/assignments/howToMakeABigCake.txt"
    third_func_file_list = []
    exeLogic.third_func(third_func_file_list)

    fourth_func_file_list = [os.path.dirname(os.path.realpath(
        __file__))+"/4thFuncGarbageFiles/junk01.txt", os.path.dirname(os.path.realpath(__file__))+"/4thFuncGarbageFiles/junk02.txt", os.path.dirname(os.path.realpath(__file__))+"/4thFuncGarbageFiles/junk03.txt"]
    exeLogic.fourth_func(fourth_func_file_list)

    fifth_func_file_list = [os.path.dirname(os.path.realpath(
        __file__))+"/5thFuncGarbageFiles/junk01.md", os.path.dirname(os.path.realpath(__file__))+"/5thFuncGarbageFiles/junk02.md"]
    exeLogic.fifth_func(fifth_func_file_list)
