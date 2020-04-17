class DataSheet(object):
    def __init__(self, courses=[]):
        self.__courses = courses

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def get_grades_as_list(self):
        return [course.optional_grade for course in self.__courses]

