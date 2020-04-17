import random
import matplotlib.pyplot as plt
from course import Course as course
from data_sheet import DataSheet as data_sheet
from student import Student as student
from exceptions import NotEnoughStudentsException

course_list = [
    course(
        name="Astrophysics",
        class_room="902",
        teacher="Henry the 2nd",
        ECTS="25",
        optional_grade="0",
    ),
    course(
        name="Fishing",
        class_room="Swimming Pool",
        teacher="Michael Jackson",
        ECTS="25",
        optional_grade="0",
    ),
    course(
        name="How to be a god",
        class_room="Olympus",
        teacher="Chronos, Titan of Time",
        ECTS="25",
        optional_grade="0",
    ),
    course(
        name="Curling",
        class_room="Cellar",
        teacher="Some random dude who usually hides in the lockers",
        ECTS="10",
        optional_grade="0",
    ),
    course(
        name="Tea Making",
        class_room="Bar Sin Sei tea shop",
        teacher="Iroh",
        ECTS="15",
        optional_grade="0",
    ),
    course(
        name="Painting",
        class_room="205",
        teacher="Bob Ross",
        ECTS="5",
        optional_grade="0",
    ),
    course(
        name="Towing",
        class_room="502",
        teacher="Jasper Smythes",
        ECTS="10",
        optional_grade="0",
    ),
    course(
        name="Math", class_room="503", teacher="Bor Ing", ECTS="20", optional_grade="0",
    ),
    course(
        name="Gymnastics",
        class_room="Janitor's Office",
        teacher="Billy Mayzeer",
        ECTS="10",
        optional_grade="0",
    ),
    course(
        name="Hunting",
        class_room="412",
        teacher="Nicholas Flammel",
        ECTS="5",
        optional_grade="0",
    ),
]
img_urls = [
    "https://scentofagamer.files.wordpress.com/2015/10/waynereynolds_ib1.jpg",
    "https://www.kcrw.com/music/shows/guest-dj-project/willem-dafoe/DSCF0981vv.jpg/@@images/1cade32b-08ed-474f-b650-24f01136cb73.jpeg"
    "https://cdna.artstation.com/p/assets/images/images/000/566/986/large/damon-woods-untitled-2.jpg?1427000340",
    "https://pbs.twimg.com/profile_images/1011280580015804420/yQ21pTwo.jpg",
]
available_grades = ["-3", "0", "2", "4", "7", "10", "12"]


def generate_random_student_list(num):
    student_list = []
    for i in range(num):
        gender_ins = ""
        if random.random() >= 0.5:
            gender_ins = "Male"
        else:
            gender_ins = "Female"
        name_ins = name_gen(gender_ins)
        courses_ins = []
        for j in range(len(course_list)):
            if random.getrandbits(1):
                copied_list = course_list.copy()
                copied_list[j - 1].optional_grade = available_grades[
                    random.randint(0, len(available_grades) - 1)
                ]
                courses_ins.append(copied_list[j - 1])
        image_ins = img_urls[random.randint(0, len(img_urls) - 1)]
        student_list.append(
            student(
                name=name_ins,
                gender=gender_ins,
                data_sheet=data_sheet(courses=courses_ins),
                image_url=image_ins,
            )
        )
    return student_list


def name_gen(gender):
    f_beginnings = [
        "Ta",
        "Ji",
        "Ja",
        "Mem",
        "La",
        "Ni",
        "Mon",
        "Ni",
        "Ka",
        "Mi",
        "Le",
        "Vi",
        "Ren",
        "E",
    ]
    f_middles = ["mi", "nun", "ren", "de", "tem", "m", "n"]
    f_ends = ["e", "t", "kun", "a", "y", "i", "nu", "mun"]

    m_beginnings = ["Ko", "Ka", "Ke", "Kra", "Kro", "ska", "Ju", "Ras", "Chu"]
    m_middles = ["rk", "v", "ar", "nd", "n", "lek"]
    m_ends = ["th", "dem", "der", "set", "zet", "put", "lak", "lek", "k", "j"]

    syllables = random.random() * 100
    name = ""

    if gender is "Male":
        if syllables <= 25:
            name = (
                m_beginnings[random.randint(0, len(m_beginnings) - 1)]
                + m_ends[random.randint(0, len(m_ends) - 1)]
            )
        elif syllables <= 65:
            name = (
                m_beginnings[random.randint(0, len(m_beginnings) - 1)]
                + m_middles[random.randint(0, len(m_middles) - 1)]
                + m_ends[random.randint(0, len(m_ends) - 1)]
            )

        elif syllables <= 90:
            name = (
                m_beginnings[random.randint(0, len(m_beginnings) - 1)]
                + m_middles[random.randint(0, len(m_middles) - 1)]
                + m_middles[random.randint(0, len(m_middles) - 1)]
                + m_ends[random.randint(0, len(m_ends) - 1)]
            )

        else:
            name = (
                m_beginnings[random.randint(0, len(m_beginnings) - 1)]
                + m_middles[random.randint(0, len(m_middles) - 1)]
                + m_middles[random.randint(0, len(m_middles) - 1)]
                + m_middles[random.randint(0, len(m_middles) - 1)]
                + m_ends[random.randint(0, len(m_ends) - 1)]
            )

    elif gender is "Female":
        if syllables <= 25:
            name = (
                f_beginnings[random.randint(0, len(f_beginnings) - 1)]
                + f_ends[random.randint(0, len(f_ends) - 1)]
            )

        elif syllables <= 65:
            name = (
                f_beginnings[random.randint(0, len(f_beginnings) - 1)]
                + f_middles[random.randint(0, len(f_middles) - 1)]
                + f_ends[random.randint(0, len(f_ends) - 1)]
            )

        elif syllables <= 90:
            name = (
                f_beginnings[random.randint(0, len(f_beginnings) - 1)]
                + f_middles[random.randint(0, len(f_middles) - 1)]
                + f_middles[random.randint(0, len(f_middles) - 1)]
                + f_ends[random.randint(0, len(f_ends) - 1)]
            )

        else:
            name = (
                f_beginnings[random.randint(0, len(f_beginnings) - 1)]
                + f_middles[random.randint(0, len(f_middles) - 1)]
                + f_middles[random.randint(0, len(f_middles) - 1)]
                + f_middles[random.randint(0, len(f_middles) - 1)]
                + f_ends[random.randint(0, len(f_ends) - 1)]
            )

    return name


def write_list_to_csv(list, output_file_string):
    """
    Writes a list of students to an output file.
    """

    with open(output_file_string, "w") as fileWrite:
        for student_person in list:
            fileWrite.write("name: " + student_person.name + "\n")
            fileWrite.write("gender: " + student_person.gender + "\n")
            fileWrite.write("courses: " + "\n\n")
            for cor in student_person.data_sheet.courses:
                fileWrite.write("course_name: " + cor.name + "\n")
                fileWrite.write("teacher: " + cor.teacher + "\n")
                fileWrite.write("ects: " + cor.ECTS + "\n")
                fileWrite.write("classroom: " + cor.class_room + "\n")
                fileWrite.write("grade: " + cor.optional_grade + "\n")
                fileWrite.write("\n")
            fileWrite.write("img_url: " + student_person.image_url + "\n")
            fileWrite.write("__________________\n\n")


def students_from_file(input_file):
    """
    Checks for line prefixes which are variables in the student object
    
    """
    student_list = []
    cList = []
    student_placeholder = {}
    courses_placeholder = {}
    lines = [line.rstrip("\n") for line in open(input_file)]
    for line in lines:
        if "____" in line:
            student_list.append(
                student(
                    name=student_placeholder["name"],
                    data_sheet=data_sheet(courses=cList.copy()),
                    gender=student_placeholder["gender"],
                    image_url=student_placeholder["image_url"],
                )
            )
            student_placeholder.clear()
            cList.clear()
        elif "name: " in line and not "_name" in line:
            student_placeholder["name"] = " ".join(line.split()[1:])
        elif "gender: " in line:
            student_placeholder["gender"] = " ".join(line.split()[1:])
        elif "course_name: " in line:
            courses_placeholder["name"] = " ".join(line.split()[1:])
        elif "teacher" in line:
            courses_placeholder["teacher"] = " ".join(line.split()[1:])
        elif "ects" in line:
            courses_placeholder["ECTS"] = " ".join(line.split()[1:])
        elif "grade" in line:
            courses_placeholder["optional_grade"] = " ".join(line.split()[1:])
            if courses_placeholder:
                cList.append(
                    course(
                        name=courses_placeholder["name"],
                        teacher=courses_placeholder["teacher"],
                        ECTS=courses_placeholder["ECTS"],
                        optional_grade=courses_placeholder["optional_grade"],
                        class_room=courses_placeholder["class_room"],
                    )
                )
                courses_placeholder.clear()
        elif "classroom" in line:
            courses_placeholder["class_room"] = " ".join(line.split()[1:])
        elif "img_url" in line:
            student_placeholder["image_url"] = " ".join(line.split()[1:])
    return student_list


def extract_requested_data(input_file):
    """
    Extracts student name, image_url and avg_grade as per 8.A + B
    """
    student_list = students_from_file(input_file)
    relevant_student_info_list = []
    for student in student_list:
        if student.data_sheet.courses:
            rel_student = {}
            rel_student["name"] = student.name
            rel_student["img_url"] = student.image_url
            rel_student["avg_grade"] = student.get_avg_grade()
            relevant_student_info_list.append(rel_student)
    student_sorted = sorted(
        relevant_student_info_list,
        reverse=True,
        key=lambda student: student["avg_grade"],
    )
    return student_sorted


def extract_top3(input_file):
    student_list = students_from_file(input_file)
    if len(student_list) < 3:
        raise NotEnoughStudentsException(
            "Method bar_char_name_pct_top3 requires atleast 3 entries"
        )
    return sorted(
        list([(student) for student in student_list]),
        reverse=True,
        key=lambda student: student.get_percentage_completed(),
    )[0:3]


def write_top3(input_file):
    student_list = students_from_file(input_file)
    try:
        if len(student_list) < 3:
            raise NotEnoughStudentsException(
                "Method bar_char_name_pct_top3 requires atleast 3 entries"
            )
        list_sorted = sorted(
            list([(student) for student in student_list]),
            reverse=True,
            key=lambda student: student.get_percentage_completed(),
        )[0:3]
        with open("top3_output.csv", "w") as fileWrite:
            for student in list_sorted:
                for key, val in student.__dict__.items():
                    if key == "_Student__data_sheet":
                        for cor in val.courses:
                            for cor_key, cor_val in cor.__dict__.items():
                                fileWrite.write(cor_key + ": " + cor_val + "\n")
                            fileWrite.write("\n")
                    else:
                        fileWrite.write(key + ": " + val + "\n")
                    fileWrite.write("\n")
                fileWrite.write("\n")
    except Exception as ex:
        print(ex)
        with open("top3_output.csv", "w") as fileWrite:
            fileWrite.write("Not enough students to generate top 3")


def ects_pct_dict_thing(input_file):
    """
    creates a dictionary of keys in 10,20,30,etc pct and values of enumerables
    extremely ugly
    can't be arsed
    """

    student_list = students_from_file(input_file)
    pct_dict = {
        "0-10%": 0,
        "10-20%": 0,
        "20-30%": 0,
        "30-40%": 0,
        "40-50%": 0,
        "50-60%": 0,
        "60-70%": 0,
        "70-80%": 0,
        "80-90%": 0,
        "90-100%": 0,
    }
    for student in student_list:
        total = student.get_percentage_completed()
        if total <= 150 * 0.1:
            pct_dict["0-10%"] = pct_dict["0-10%"] + 1
        elif total <= 150 * 0.2:
            pct_dict["10-20%"] = pct_dict["10-20%"] + 1
        elif total <= 150 * 0.3:
            pct_dict["20-30%"] = pct_dict["20-30%"] + 1
        elif total <= 150 * 0.4:
            pct_dict["30-40%"] = pct_dict["30-40%"] + 1
        elif total <= 150 * 0.5:
            pct_dict["40-50%"] = pct_dict["40-50%"] + 1
        elif total <= 150 * 0.6:
            pct_dict["50-60%"] = pct_dict["50-60%"] + 1
        elif total <= 150 * 0.7:
            pct_dict["60-70%"] = pct_dict["60-70%"] + 1
        elif total <= 150 * 0.8:
            pct_dict["70-80%"] = pct_dict["70-80%"] + 1
        elif total <= 150 * 0.9:
            pct_dict["80-90%"] = pct_dict["80-90%"] + 1
        else:
            pct_dict["90-100%"] = pct_dict["90-100%"] + 1
    return pct_dict


def course_attendents_count(student_list):
    c_dict = {key.name: 0 for key in course_list}
    for student in student_list:
        for cor in student.data_sheet.courses:
            c_dict[cor.name] = c_dict[cor.name] + 1
    return c_dict
