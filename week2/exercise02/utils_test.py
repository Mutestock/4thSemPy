
import os
import exercise_logic as exeLogic

if __name__ == "__main__":
    exeLogic.first_func(os.path.dirname(os.path.realpath(__file__)))
    exeLogic.second_func(os.path.dirname(os.path.realpath(__file__)))

    third_func_file_list = [
        "C:/Users/Henning/Desktop/FoxyBoxesMainFolder/playlistOrganizerProjectNotes.txt", "C:/Users/Henning/Desktop/FoxyBoxesMainFolder/Foxy Boxes/backup/pre_restplus_rebuild/amb/src/ambAPI/schema/playlist_schema.py"]
    exeLogic.third_func(third_func_file_list)

    fourth_func_file_list = [os.path.dirname(os.path.realpath(
        __file__))+"/4thFuncGarbageFiles/junk01.txt", os.path.dirname(os.path.realpath(__file__))+"/4thFuncGarbageFiles/junk02.txt", os.path.dirname(os.path.realpath(__file__))+"/4thFuncGarbageFiles/junk03.txt"]
    exeLogic.fourth_func(fourth_func_file_list)

    fifth_func_file_list = [os.path.dirname(os.path.realpath(
        __file__))+"/5thFuncGarbageFiles/junk01.md", os.path.dirname(os.path.realpath(__file__))+"/5thFuncGarbageFiles/junk02.md"]
    exeLogic.fifth_func(fifth_func_file_list)
