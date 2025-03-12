# Import necessary libraries
import libraries


def student_enrollment():
    print("Student Enrollment")
    print("1) Enroll Student")
    print("2) Remove Student")

    # Ask user to choose an option
    choice = int(input("Enter choice: "))

    while True:
        if choice == 1:  # Enrolling a student
            try:
                # Open and read classes.txt file
                with open("classes.txt", "r") as file:
                    lines = file.readlines()

                    # Convert each line into a list, skipping empty lines
                    classes = [line.strip().split(",") for line in lines]

                    # If no classes are available
                    if len(classes) <= 1:
                        print("No available classes.")
                        return

                        # Extract class IDs from available classes
                    class_ids = [cls[0] for cls in classes[1:]]
                    print("Available Classes:", class_ids)

                # Ask user to enter class ID
                class_id = input("Enter class ID: ").strip()
                if class_id in class_ids:
                    try:
                        # Open and read students.txt file
                        with open("students.txt", "r") as file:
                            lines = file.readlines()

                            # Convert each line into a list
                            students = [line.strip().split(",") for line in lines]

                        # If no students are available
                        if len(students) <= 1:
                            print("No available students.")
                            return

                            # Extract student IDs
                        student_ids = [student[0] for student in students[1:]]
                        print("Students:", student_ids)
                    except FileNotFoundError:
                        print("students.txt file not found.")
                        return

                        # Ask user to enter student ID
                    student_id = input("Enter Student ID: ").strip()
                    if student_id in student_ids:
                        try:
                            # Open and read assessments.txt file
                            with open("assessments.txt", "r") as file:
                                lines = file.readlines()

                                # Convert each line into a list
                                assignments = [line.strip().split(",") for line in lines]

                            # If no assignments are available
                            if len(assignments) <= 1:
                                print("No available assignments.")
                                return

                                # Extract assignment IDs
                            assignment_ids = [row[0] for row in assignments[1:]]
                            print("Assignments:", assignment_ids)
                        except FileNotFoundError:
                            print("assessments.txt file not found.")
                            return

                            # Ask user to enter an assignment ID
                        assignment = input("Enter Assignment ID: ").strip()
                        if assignment in assignment_ids:
                            # Ask user to enter enrollment status
                            status = input("Enter Status (Enrolled/Unenroll): ").strip().capitalize()
                            if status not in ["Enrolled", "Unenroll"]:
                                print("Invalid status. Please enter 'Enrolled' or 'Unenroll'.")
                                return

                                # Generate new enrollment ID
                            course_enrollment_id = libraries.generate_new_id("course_enrollments.txt", "CE")

                            # Save new enrollment record to file
                            with open("course_enrollments.txt", "a") as file:
                                file.write(f"{course_enrollment_id},{class_id},{student_id},{assignment},{status}\n")
                            print("Enrolled successfully.")
                            return
                        else:
                            print("Assignment ID not found.")
                            continue
                    else:
                        print("Student ID not found.")
                        continue
                else:
                    print("Class ID not found.")
                    continue
            except FileNotFoundError:
                print("classes.txt file not found.")
                continue

        elif choice == 2:  # Removing a student from a class
            try:
                # Open and read classes.txt file
                with open("classes.txt", "r") as file:
                    lines = file.readlines()

                    # Convert each line into a list
                    classes = [line.strip().split(",") for line in lines]

                    # If no classes are available
                    if len(classes) <= 1:
                        print("No available classes.")
                        return

                        # Extract class IDs
                    class_ids = [cls[0] for cls in classes[1:]]
                    print("Available Classes:", class_ids)
            except FileNotFoundError:
                print("classes.txt file not found.")
                return

                # Ask user to enter class ID
            class_id = input("Enter class ID: ").strip()
            if class_id in class_ids:
                try:
                    # Open and read students.txt file
                    with open("students.txt", "r") as file:
                        lines = file.readlines()

                        # Convert each line into a list
                        students = [line.strip().split(",") for line in lines]

                    # If no students are available
                    if len(students) <= 1:
                        print("No available students.")
                        return

                        # Extract student IDs
                    student_ids = [student[0] for student in students[1:]]
                    print("Students:", student_ids)
                except FileNotFoundError:
                    print("students.txt file not found.")
                    return

                    # Ask user to enter student ID
                student_id = input("Enter Student ID: ").strip()
                if student_id in student_ids:
                    # Open course_enrollments.txt to remove the student enrollment
                    with open("course_enrollments.txt", "r") as file:
                        enrollments = file.readlines()

                    # Rewrite the file without the removed enrollment
                    with open("course_enrollments.txt", "w") as file:
                        for enrollment in enrollments:
                            if f"{student_id},{class_id}" not in enrollment.strip():
                                file.write(enrollment)

                    print("Removed successfully.")
                else:
                    print("Student ID not found.")
            else:
                print("Class ID not found.")

        else:
            print("Invalid Choice")


student_enrollment()