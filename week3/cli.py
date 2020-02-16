import click
import logic
import logging
import charts
from pprint import pprint


@click.group()
def manager():
    pass


@manager.command()
@click.option("--write", "-w")
@click.option("--read", "-r", type=click.Choice(["all", "avg"], case_sensitive=False))
@click.option(
    "--graph",
    "-g",
    type=click.Choice(
        ["avg", "pct", "pct3", "pie", "count", "count2"], case_sensitive=False
    ),
)
def student(write, read, graph):
    if write == "pct3":
        logic.write_top3("student_output.csv")
    elif write:
        try:
            logic.write_list_to_csv(
                logic.generate_random_student_list(int(write)), "student_output.csv"
            )
        except Exception as ex:
            logging.exception("Error in CLI generate random student list")
    elif read == "all":
        try:
            student_list = logic.students_from_file("student_output.csv")
            for student in student_list:
                print(vars(student))
                for i, d_sheet in enumerate(student.data_sheet.courses):
                    print(vars(d_sheet))
                    print(i)
        except Exception as ex:
            logging.exception("Error in CLI read students from file")
    elif read == "avg":
        try:
            student_list = logic.extract_requested_data("student_output.csv")
            for student in student_list:
                print()
                for key, val in student.items():
                    print("{}: {}".format(key, val))
        except Exception as ex:
            logging.exception("Error in CLI students avg")
    if graph == "avg":
        charts.bar_chart_name_avg_grade("student_output.csv")
    elif graph == "pct":
        charts.bar_chart_name_pct("student_output.csv")
    elif graph == "pct3":
        charts.bar_char_name_pct_top3("student_output.csv")
    elif graph == "pie":
        charts.pie_ects_pct("student_output.csv")
    elif graph == "count":
        charts.bar_course_attendance_count("student_output.csv")
    elif graph == "count2":
        charts.bar_course_attendance_count_gender("student_output.csv")
