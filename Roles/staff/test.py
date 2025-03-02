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

