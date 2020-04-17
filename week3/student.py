class Student(object):
    def __init__(self, name, gender, data_sheet, image_url):
        self.__name = name
        self.__gender = gender
        self.__data_sheet = data_sheet
        self.__image_url = image_url

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.gender = gender

    @property
    def data_sheet(self):
        return self.__data_sheet

    @data_sheet.setter
    def data_sheet(self, data_sheet):
        self.__data_sheet = data_sheet

    @property
    def image_url(self):
        return self.__image_url

    @data_sheet.setter
    def data_sheet(self, image_url):
        self.__image_url = image_url

    def get_avg_grade(self):
        return sum(
            [int(grade.optional_grade) for grade in self.__data_sheet.courses]
        ) / len(self.__data_sheet.courses)

    def get_percentage_completed(self):
        passed_ects = sum(
            [
                int(course.ECTS)
                for course in self.__data_sheet.courses
                if ((int(course.ECTS)) >= 2)
            ]
        )
        return passed_ects / 150 * 100

    def get_list_of_courses(self):
        return self.__data_sheet.courses
