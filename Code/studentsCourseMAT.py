def announcements(student_id):
    try:
        with open("../Data/course_enrollments.txt", "r") as f:
            course_enrollments = f.readlines()[1:]

        with open("../Data/classes.txt", "r") as f:
            classes = f.readlines()[1:]

        print("\n============================ Announcements ===========================")
        for enrollment in course_enrollments:
            enrollment_data = enrollment.strip().split(",")
            if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                class_id = enrollment_data[1]
                for classes_info in classes:
                    classes_data = classes_info.strip().split(",")
                    if classes_data[0] == class_id:
                        print(f"\n{classes_data[0]}-{classes_data[1]} | {classes_data[7]}")
                        print(f"{classes_data[9]}")
                        print(" ")
    except FileNotFoundError:
        print("Data not found.")
        
    print("=======================================================================")
    print("0 | Previous Page")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourseMAT(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")

def assignments(student_id): # materials.txt
    try:
        with open("../Data/course_enrollments.txt", "r") as f:
            course_enrollments = f.readlines()[1:]

        with open("../Data/classes.txt", "r") as f:
            classes = f.readlines()[1:]

        with open("../Data/materials.txt", "r") as f:
            materials = [line.strip().split(",") for line in f.readlines()[1:]]

        with open("../Data/courses.txt", "r") as f:
            courses = {line.split(",")[0]: line.split(",")[1] for line in f.readlines()[1:]}

        print("====================== Assignments Materials ======================")
        for enrollment in course_enrollments:
            enrollment_data = enrollment.strip().split(",")
            if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                class_id = enrollment_data[1]
                for classes_info in classes:
                    classes_data = classes_info.strip().split(",")
                    if classes_data[0] == class_id:
                        course_id = classes_data[1]
                        course_name = courses.get(course_id)
                        print(f"\n{course_name} ({classes_data[1]}-{classes_data[0]})")
                        for material in materials:
                            material_data = material
                            if material_data[1] == course_id:
                                print(f"□ {material_data[3]}")
                        print(" ")

    except FileNotFoundError:
        print("Data not found.")
        
    print("===================================================================")

def lecture_notes(student_id): # classes.txt
    try:
        with open("../Data/course_enrollments.txt", "r") as f:
            course_enrollments = f.readlines()[1:]

        with open("../Data/classes.txt", "r") as f:
            classes = f.readlines()[1:]

        print("\n============================ Course Notes ===========================")
        for enrollment in course_enrollments:
            enrollment_data = enrollment.strip().split(",")
            if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                class_id = enrollment_data[1]
                for classes_info in classes:
                    classes_data = classes_info.strip().split(",")
                    if classes_data[0] == class_id:
                        print(f"\n{classes_data[0]}-{classes_data[1]} | {classes_data[7]}")
                        print(f"{classes_data[8]}")
                        print(" ")
    except FileNotFoundError:
        print("Data not found.")
        
    print("=======================================================================")
    print("0 | Previous Page")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourseMAT(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")

def course_materials(student_id):
    try:
        with open("../Data/course_enrollments.txt", "r") as f:
            course_enrollments = f.readlines()[1:]

        with open("../Data/classes.txt", "r") as f:
            classes = f.readlines()[1:]

        with open("../Data/materials.txt", "r") as f:
            materials = [line.strip().split(",") for line in f.readlines()[1:]]

        with open("../Data/courses.txt", "r") as f:
            courses = {line.split(",")[0]: line.split(",")[1] for line in f.readlines()[1:]}

        print("\n============================ Course Materials ===========================")
        for enrollment in course_enrollments:
            enrollment_data = enrollment.strip().split(",")
            if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                class_id = enrollment_data[1]
                for classes_info in classes:
                    classes_data = classes_info.strip().split(",")
                    if classes_data[0] == class_id:
                        course_id = classes_data[1]
                        course_name = courses.get(course_id)
                        print(f"\n{course_name} ({classes_data[1]}-{classes_data[0]})")
                        for material in materials:
                            material_data = material
                            if material_data[1] == course_id:
                                print(f"□ {material_data[2]}")
                        print(" ")

    except FileNotFoundError:
        print("Data not found.")
        
    print("=========================================================================")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourseMAT(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")
            
def studentsCourseMAT(student_id):
    with open("../Data/students.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == student_id:
                student_details = data
                
    print("\n======== Course Materials ========")
    print(f"Student ID: {student_id}\nStudent Name: {student_details[1]}\nEnrollment Status: {student_details[6]}")
    print("===================================")
    print("|    1 | Course Materials         |")
    print("|    2 | Lecture Notes            |")
    print("|    3 | Assignment Materials     |")
    print("|    4 | Announcements            |")
    print("|    0 | Previous Page            |")
    print("===================================")
    choice = input("Please enter an option (0~4): ")
    if choice == "1":
        course_materials(student_id)
    elif choice == "2":
        lecture_notes(student_id)
    elif choice == "3":
        assignments(student_id)
    elif choice == "4":
        announcements(student_id)
    elif choice == "0":
        import students
        students.students(student_id)
        return
    else:
        print("\nPlease try again and enter a valid choice.\n")