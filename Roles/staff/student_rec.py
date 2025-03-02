import staff_lib
import color

def student_rec():
    """Display student record menu and process user choices."""
    while True:
        print(f"{'=' * 17}{color.BOLD}{color.BLUE} STUDENT RECORDS {color.RESET}{'=' * 18}")
        print(f"""{" " * 9}{color.YELLOW}1.{color.RESET}  Students' Course Registration
{" " * 9}{color.YELLOW}2.{color.RESET}  Transfer Course
{" " * 9}{color.YELLOW}3.{color.RESET}  Course Withdrawal
{" " * 9}{color.YELLOW}0.{color.RESET}  Back""")
        print(f"{'=' * 52}")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3])
        print()

        if choice == 1:
            stu_course_reg()
        elif choice == 2:
            stu_trans_course()
        elif choice == 3:
            stu_course_withdraw()
        elif choice == 0:
            return  # Return to staff menu


def stu_course_reg():
    """
    This function allows a staff member to register a student for a course. 
    It handles displaying available courses, selecting a course, selecting a class, and enrolling the student in the chosen class.
    """
    try:
        print(f"{'=' * 10}{color.BOLD}{color.BLUE} STUDENTS' COURSE REGISTRATION {color.RESET}{'=' * 11}")

        with open("./Data/courses.txt", "r") as courses:
            header = courses.readline().strip().split(",")

            # Calculate column widths based on header
            col_widths = [len(col) for col in header]
            records = []

            for course in courses:
                try:
                    fields = staff_lib.read_csv_line(course.strip())

                    if len(fields) != len(header):
                        continue

                    records.append(fields)

                    # Update column width based on data length
                    for i in range(len(fields)):
                        col_widths[i] = max(col_widths[i], len(fields[i]))

                except ValueError:
                    continue

        # Print table header
        header_row = " | ".join(f"{color.BOLD}{header[i].upper():<{col_widths[i]}}{color.RESET}" for i in range(len(header)))
        print(f"{color.YELLOW}{'-' * len(header_row)}{color.RESET}")
        print(header_row)
        print(f"{color.YELLOW}{'-' * len(header_row)}{color.RESET}")

        # Print table rows
        for record in records:
            row = " | ".join(f"{record[i]:<{col_widths[i]}}" for i in range(len(record)))
            print(row)

        print(f"{color.YELLOW}{'-' * len(header_row)}{color.RESET}")

        while True:
            course_chosen = input(f"{color.GREEN}Enter chosen course ID (0 to cancel): {color.RESET}").strip()
            if course_chosen == "0":
                return
            if staff_lib.search_value("./Data/courses.txt", 0, course_chosen):
                with open("./Data/classes.txt", "r") as classes:
                    class_header = classes.readline().strip().split(",")

                    # Print table header for classes
                    print(f"{color.YELLOW}{'-' * 30}{color.RESET}")
                    print(f"{color.BOLD}CLASS_ID | TEACHER_NAME{color.RESET}")
                    print(f"{color.YELLOW}{'-' * 30}{color.RESET}")

                    for class_rec in classes:
                        try:
                            class_field = staff_lib.read_csv_line(class_rec.strip())

                            if len(class_field) != len(class_header):
                                continue
                            
                            if class_field[1] == course_chosen:
                                teacher_name = staff_lib.search_value("./Data/teachers.txt", 0, class_field[2], 1)
                                if not teacher_name:
                                    continue
                                print(f"{class_field[0]:<8} | {teacher_name}")
                        except ValueError:
                            continue
                print(f"{color.YELLOW}{'-' * 30}{color.RESET}")
                break
            else:
                print(f"{color.RED}Invalid input. Please try again.{color.RESET}")

        while True:
            class_chosen = input(f"{color.GREEN}Enter class ID chosen (0 to cancel): {color.RESET}").strip()

            if class_chosen == "0":
                return
            
            if staff_lib.search_value("./Data/classes.txt", 0, class_chosen):
                student_id = input(f"{color.GREEN}Enter student ID (0 to cancel): {color.RESET}").strip()

                if student_id == "0":
                    return
                
                if staff_lib.search_value("./Data/students.txt", 0, student_id):
                    course_enroll, _ = staff_lib.read_csv_file("./Data/course_enrollments.txt")

                    already_enrolled = any(
                        enroll["student_id"] == student_id and enroll["class_id"] == class_chosen and enroll["course_enroll_status"] == "Enrolled"
                        for enroll in course_enroll
                    )

                    if already_enrolled:
                        print(f"{color.RED}Student has already enrolled in this class.{color.RESET}")
                        return

                    course_enroll, header = staff_lib.read_csv_file("./Data/course_enrollments.txt")

                    if course_enroll:
                        last_id = course_enroll[-1]["course_enrollment_id"]
                        next_id = staff_lib.new_id(last_id, 2)
                    else: 
                        next_id = "CE001"

                    break
                else:
                    print(f"{color.RED}Invalid student ID. Please try again.{color.RESET}")
                    continue
            else:
                print(f"{color.RED}Invalid class ID. Please try again.{color.RESET}")
                continue
        
        with open("./Data/course_enrollments.txt", "a") as new_rec:
            new_rec.write(f"{next_id},{class_chosen},{student_id},None,Enrolled\n")

        print(f"{color.GREEN}Successfully enrolled!{color.RESET}")

    except FileNotFoundError:
        print(f"{color.RED}File not found.{color.RESET}")
    except IOError:
        print(f"{color.RED}Unable to read/write the file.{color.RESET}")

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