import matplotlib.pyplot as plt
from course import Course as course
from data_sheet import DataSheet as data_sheet
from student import Student as student
from logic import (
    extract_requested_data,
    students_from_file,
    extract_top3,
    ects_pct_dict_thing,
    course_attendents_count,
    course_list,
)
from exceptions import NotEnoughStudentsException


def bar_chart_name_avg_grade(input_file):
    student_list = extract_requested_data(input_file)
    plt.bar(
        list([student["name"] for student in student_list]),
        list([student["avg_grade"] for student in student_list]),
        width=1,
        align="center",
    )
    plt.xticks(
        list([student["name"] for student in student_list]),
        rotation="vertical",
        fontsize=5,
    )
    plt.title("Student/avg_grade")
    plt.xlabel("Student Names", fontsize=11)
    plt.ylabel("avg_grade", fontsize=11)
    plt.ylim(0, 12)
    plt.show()


def bar_chart_name_pct(input_file):
    student_list = students_from_file(input_file)
    plt.bar(
        list([student.name for student in student_list]),
        list([(student.get_percentage_completed()) for student in student_list]),
        width=1,
        align="edge",
    )
    plt.xticks(
        list([student.name for student in student_list]),
        rotation="vertical",
        fontsize=5,
    )
    plt.title("Student/Percentage")
    plt.xlabel("Student Names", fontsize=11)
    plt.ylabel("Percentage", fontsize=11)
    plt.ylim(0, 100)
    plt.show()


def bar_char_name_pct_top3(input_file):
    list_sorted = extract_top3(input_file)
    plt.bar(
        list([student.name for student in list_sorted]),
        list([student.get_percentage_completed() for student in list_sorted]),
        # width=0.25,
        # align="edge",
    )
    plt.xticks(
        list([student.name for student in list_sorted]),
        rotation="vertical",
        fontsize=5,
    )
    plt.title("Student/Percentage top 3")
    plt.xlabel("Student Names", fontsize=11)
    plt.ylabel("Percentage", fontsize=11)
    plt.ylim(0, 100)
    plt.show()


def pie_ects_pct(input_file):
    pct_dict = ects_pct_dict_thing(input_file)
    fig, ax = plt.subplots()
    ax.pie(pct_dict.values())
    ax.set_aspect("equal")
    ax.legend(pct_dict.keys(), loc="upper right")
    plt.show()


def bar_course_attendance_count(input_file):
    list_course = course_attendents_count(students_from_file(input_file))
    plt.bar(list_course.keys(), list_course.values())
    plt.title("Course count")
    plt.xticks(list(list_course.keys()), rotation="vertical", fontsize=10)
    plt.ylabel("Course count")
    plt.xlabel("Course name")
    plt.show()


def bar_course_attendance_count_gender(input_file):
    student_list = students_from_file(input_file)
    male_list = [student for student in student_list if student.gender == "Male"]
    female_list = [student for student in student_list if student.gender == "Female"]
    course_names = [course.name for course in course_list]
    male_count = course_attendents_count(male_list)
    female_count = course_attendents_count(female_list)

    bar1 = plt.bar(list(male_count.keys()), list(male_count.values()), color="blue")
    plt.title("Course Attendance per gender")
    plt.xlabel("Courses", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    plt.tick_params(axis="both", which="minor", labelsize=10)
    bar2 = plt.bar(
        female_count.keys(),
        female_count.values(),
        color="red",
        bottom=list(male_count.values()),
    )
    plt.legend([bar1, bar2], ["Male", "Female"], loc="upper right")
    plt.show()
