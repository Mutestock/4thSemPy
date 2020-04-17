class Course(object):
    def __init__(self, name, class_room, teacher, ECTS, optional_grade):
        self.__name = name
        self.__class_room = class_room
        self.__teacher = teacher
        self.__ECTS = ECTS
        self.__optional_grade = optional_grade

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def class_room(self):
        return self.__class_room

    @class_room.setter
    def class_room(self, class_room):
        self.__class_room = class_room

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        self.__teacher = teacher

    @property
    def ECTS(self):
        return self.__ECTS

    @ECTS.setter
    def ECTS(self, ECTS):
        self.__ETCS = ECTS

    @property
    def optional_grade(self):
        return self.__optional_grade

    @optional_grade.setter
    def optional_grade(self, optional_grade):
        self.__optional_grade = optional_grade

