"""This is a Staff's code."""

import staff_lib
import staff_color as color

def student_rec():
    """Display student record menu and processes user choices."""
    while True:
        print(f"{"=" * 17}{color.BOLD}{color.BLUE} STUDENT RECORDS {color.RESET}{"=" * 18}")
        print(f"""{" " * 10}{color.YELLOW}1.{color.RESET} Students' Course Registration
{" " * 10}{color.YELLOW}2.{color.RESET} Transfer Course
{" " * 10}{color.YELLOW}3.{color.RESET} Course Withdrawal
{" " * 10}{color.YELLOW}0.{color.RESET} Back""")
        print(f"=" * 52)
        
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
        print(f"{'=' * 35}{color.BOLD}{color.BLUE} STUDENTS' COURSE REGISTRATION {color.RESET}{'=' * 34}")
        with open("./Data/courses.txt", "r") as courses:
            header = courses.readline().strip().split(",")
            print(f"{color.YELLOW}Available Courses:{color.RESET}")
            print("-" * 100)
            for col_name in header:
                print(f"{color.BOLD}{col_name.replace("_", " ").upper()}{' ' * 15}{color.RESET}", end='')
            print()
            print("-" * 100)
            for course in courses:
                try:
                    # Pass the line (record) into staff_lib.read_csv_line and assign the return value (a list) into a variable
                    fields = staff_lib.read_csv_line(course.strip())

                    # Skip the line if the line does not have the same number of column as header
                    if len(fields) != len(header):
                        continue

                    print(f"{' '*10}".join(fields))
                    print("-" * 100)

                except ValueError:
                    continue
        while True:
            # User input course_id, check if is valid (in courses_id), display classes with that course_id together with teacher name
            course_chosen = input(f"{color.GREEN}Enter chosen course ID (0 to cancel): {color.RESET}").strip()
            print()
            if course_chosen == "0":
                return
            if staff_lib.search_value("./Data/courses.txt", 0, course_chosen):
                with open("./Data/classes.txt", "r") as classes:
                    class_header = classes.readline().strip().split(",")
                    print(f"{color.YELLOW}Availables Classes:{color.RESET}")
                    print("-" * 25)
                    print(f"{color.BOLD}CLASS ID  TEACHER NAME{color.RESET}")
                    print("-" * 25)
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
                                print(class_field[0], teacher_name, sep="    ")
                                print("-" * 25)
                        except ValueError:
                            continue
                break
            else:
                print("Invalid input. Please try again")

        while True:
            class_chosen = input(f"{color.GREEN}Enter class ID (0 to cancel): {color.RESET}").strip()
            print()

            if class_chosen == "0": # Cancelled attempt
                return
            
            # Verify if the class ID exists in classes.txt
            if staff_lib.search_value("./Data/classes.txt", 0, class_chosen):
                student_id = input(f"{color.GREEN}Enter student ID (0 to cancel): {color.RESET}").strip()
                print()

                if student_id == "0": # Cancelled attempt
                    return
                
                # Verify if the student ID exist in students.txt
                if staff_lib.search_value("./Data/students.txt", 0, student_id):

                    # Read all enrollments from the file
                    course_enroll, _ = staff_lib.read_csv_file("./Data/course_enrollments.txt")

                    # Initialize a flag to check if the student is already enrolled
                    already_enrolled = False

                    # Loop through each enrollment record
                    for enroll in course_enroll:
                        # Check if this record matches the student, class, and has "Enrolled" status
                        if enroll["student_id"] == student_id and enroll["class_id"] == class_chosen and enroll["course_enroll_status"] == "Enrolled":
                            already_enrolled = True
                            break 

                    # Prevent duplication enrollment
                    if already_enrolled:
                        print(f"{color.RED}Student is already enrolled in this class.{color.RESET}")
                        print()
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
                    print(f"{color.RED}Invalid student ID. Please try again.{color.RESET}")
                    print()
                    continue
            else:
                print(f"{color.RED}Invalid class ID. Please try again.{color.RESET}")
                print()
                continue
        
        # Add new record
        with open("./Data/course_enrollments.txt", "a") as new_rec:
            new_rec.write(f"{next_id},{class_chosen},{student_id},None,Enrolled\n")
        print(f"{color.GREEN}Student successfully enrolled!{color.RESET}")
        print()
                        
    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    # Return back to student record menu
    return


def stu_course_withdraw():
    """Transfer students from one course to another"""
    while True:
        try:
            student_id = input(F"{color.GREEN}Enter student ID (0 to cancel): {color.RESET}").strip()
            print()
            if student_id == "0":
                return # Return back to student record menu
            
            # Checks if student enrolled in any course
            elif not staff_lib.search_value("./Data/course_enrollments.txt", 2, student_id):
                print(f"{color.RED}Invalid student ID. Please try again.{color.RESET}")
                print()
                continue
            
            # Get the class_id(s) students enrolled in (a list)
            classes_id = staff_lib.search_value("./Data/course_enrollments.txt", 2, student_id, 1)

            # Read from classes.txt
            classes, class_header = staff_lib.read_csv_file("./Data/classes.txt")

            print(f"{color.YELLOW}Classes Student Enrolled In:{color.RESET}")
            print("-" * 50)
            print(f"{color.BOLD}CLASS ID  COURSE NAME{color.RESET}")
            print("-" * 50)

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
                        print(rec["class_id"], course, sep="    ")
                        print("-" * 50)

            while True:
                course_from = input(f"{color.GREEN}Enter class id student wants to withdraw (0 to cancel): {color.RESET}").strip()
                print()
                if course_from == "0":
                    return
                elif course_from not in classes_id:
                    print(f"{color.RED}Invalid class ID. Please try again.{color.RESET}")
                    print()
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
                    print(f"{color.GREEN}Successfully unenrolled course.{color.RESET}")
                    print()
                break
            break
                 
        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return


def stu_trans_course():
    print(f"{color.BLUE}TRANSFER COURSE{color.RESET}")
    stu_course_withdraw()
    stu_course_reg()