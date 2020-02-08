import os

# __dir_path = os.path.dirname(os.path.realpath(__file__))


class non_essential_qol():
    '''
    Utilities like creating a downloads folder in the repo to prevent filling the main folder with files.
    This is a bit of a test when it comes to static methods.
    '''

    @staticmethod
    def __file_directory_generation():
        try:
            os.mkdir("downloads")
            print("Directory created...")
        except FileExistsError:
            print("Directory 'downloads' already exists")

    @staticmethod
    def qol_setup():
        non_essential_qol.__file_directory_generation()

    @staticmethod
    def file_name_handling(file):
        fileExtensionArr = file.split('/')
        return fileExtensionArr[len(fileExtensionArr)-1]
