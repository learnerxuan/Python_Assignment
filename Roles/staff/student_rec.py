import staff_lib


def student_rec():
    """Display student record menu and processes user choices."""
    while True:
        print("""
1. Students' Course Registration
2. Transfer Course
3. Course Withdrawal
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3])

        if choice == 1:
            stu_course_reg()
        elif choice == 2:
            stu_trans_course()
        elif choice == 3:
            stu_course_withdraw()
        elif choice == 0:
            # Return back to staff menu
            return
            

def stu_course_reg():
    """
    This function allows a staff member to register a student for a course. 
    It handles displaying available courses, selecting a course, selecting a class, and enrolling the student in the chosen class
    """
    try:
        with open("./Data/courses.txt", "r") as courses:
            header = courses.readline().strip().split(",")
            print(','.join(header))
            for course in courses:
                try:
                    # Pass the line (record) into staff_lib.read_csv_line and assign the return value (a list) into a variable
                    fields = staff_lib.read_csv_line(course.strip())

                    # Skip the line if the line does not have the same number of column as header
                    if len(fields) != len(header):
                        continue

                    print(','.join(fields))
                except ValueError:
                    continue
        while True:
            # User input course_id, check if is valid (in courses_id), display classes with that course_id together with teacher name
            course_chosen = input("Enter chosen course ID (0 to cancel): ").strip()
            if course_chosen == "0":
                return
            if staff_lib.search_value("./Data/courses.txt", 0, course_chosen):
                with open("./Data/classes.txt", "r") as classes:
                    class_header = classes.readline().strip().split(",")
                    print("class_id,teacher_name")
                    for class_rec in classes:
                        try:
                            # Pass the line (record) into staff_lib.read_csv_line and assign the return value (a list) into a variable
                            class_field = staff_lib.read_csv_line(class_rec.strip())

                            # Skip the line if the line does not have the same number of column as header
                            if len(class_field) != len(class_header):
                                continue
                            
                            # Find teacher name in teachers.txt using corresponding teacher_id in classes.txt
                            if class_field[1] == course_chosen:
                                teacher_name = staff_lib.search_value("./Data/teachers.txt", 0, class_field[2], 1)
                                if not teacher_name:
                                    continue
                                print(class_field[0], teacher_name, sep=",")
                        except ValueError:
                            continue
                break
            else:
                print("Invalid input. Please try again")

        while True:
            class_chosen = input("Enter class ID chosen (0 to cancell): ").strip()

            if class_chosen == "0": # Cancelled attempt
                return
            
            # Verify if the class ID exists in classes.txt
            if staff_lib.search_value("./Data/classes.txt", 0, class_chosen):
                student_id = input("Enter student ID (0 to cancel): ").strip()

                if student_id == "0": # Cancelled attempt
                    return
                
                # Verify if the student ID exist in students.txt
                if staff_lib.search_value("./Data/students.txt", 0, student_id):

                    # Use search_value to check if the student is already enrolled in this class with status "Enrolled"
                    existing_enrollment = staff_lib.search_value("./Data/course_enrollments.txt", 2, student_id, 1)

                    if existing_enrollment:
                        # Check the status of the existing enrollment (Enrolled or other)
                        enroll_status = staff_lib.search_value("./Data/course_enrollments.txt", 2, student_id, 4)
                        if enroll_status == "Enrolled" and existing_enrollment == class_chosen:
                            print(f"Student has already enrolled in this class.")
                            return

                    # Read from course_enrollments.txt
                    course_enroll, header = staff_lib.read_csv_file("./Data/course_enrollments.txt")

                    if course_enroll:  # Check if the list is not empty
                        last_id = course_enroll[-1]["course_enrollment_id"]
                        next_id = staff_lib.new_id(last_id, 2)  # Increment ID
                    else: 
                        next_id = "CE001"  # Default starting ID if no records exist
                    break
                else:
                    print("Invalid student ID. Please try again.")
                    continue
            else:
                print("Invalid class ID. Please try again")
                continue
        
        # Add new record
        with open("./Data/course_enrollments.txt", "a") as new_rec:
            new_rec.write(f"{next_id},{class_chosen},{student_id},None,Enrolled\n")
        print("Successfully enrolled!")
                        
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    # Return back to student record menu
    return


def stu_course_withdraw():
    """Transfer students from one course to another"""
    while True:
        try:
            student_id = input("Enter student ID (0 to cancel): ").strip()
            if student_id == "0":
                return # Return back to student record menu
            
            # Checks if student enrolled in any course
            elif not staff_lib.search_value("./Data/course_enrollments.txt", 2, student_id):
                print("Invalid student ID. Please try again.")
                continue
            
            # Get the class_id(s) students enrolled in (a list)
            classes_id = staff_lib.search_value("./Data/course_enrollments.txt", 2, student_id, 1)

            # Read from classes.txt
            classes, class_header = staff_lib.read_csv_file("./Data/classes.txt")

            # Iterate every record in classes.txt
            for rec in classes:
                # If class is enrolled by student
                if rec["class_id"] in classes_id:
                    # Check enrollment status 
                    course_status = staff_lib.search_value("./Data/course_enrollments.txt", 1, rec["class_id"], 4)

                    if course_status != "Unenrolled":
                        # Get the corresponding course name from courses.txt
                        course = staff_lib.search_value("./Data/courses.txt", 0, rec["course_id"], 1)
                        # Print the class id together with course name
                        print(rec["class_id"], course, sep=",")

            while True:
                course_from = input("Enter class id student wants to withdraw (0 to cancel): ").strip()
                if course_from == "0":
                    return
                elif course_from not in classes_id:
                    print("Invalid class ID. Please try again.")
                    continue
                course_enroll, course_header = staff_lib.read_csv_file("./Data/course_enrollments.txt")

                # Get to the record line that student wish to withdraw
                for line in course_enroll:
                    if line["class_id"] == course_from and line["student_id"] == student_id:
                        line["course_enroll_status"] = "Unenrolled"

                with open("./Data/course_enrollments.txt", "w") as writer:
                    writer.write(",".join(course_header) + "\n")
                    for line in course_enroll:
                        # Only write the value of each key-value pair
                        writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in line.values()) + "\n")
                    print("Successfully unenrolled course.")
                break
            break
                 
        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file")

    return


def stu_trans_course():
    stu_course_withdraw()
    stu_course_reg()