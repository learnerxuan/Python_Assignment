# Import necessary libraries
import libraries  

def grade_assignment(teacher_id):
    print("Grading and Assessment")
    print("1) Grade Assignment")
    print("2) Grade Exams")
    print("3) Provide Feedback")

    # Ask user to choose an option
    choice = input("Enter choice: ").strip()

    while True:
        if choice == "1" or choice == "2":  # If the user chooses to grade an assignment or an exam
            try:
                # Open and read classes.txt file
                with open("classes.txt", "r") as file:
                    lines = file.readlines()
                    classes = [line.strip().split(",") for line in lines]

                # Check if there are available classes
                if len(classes) <= 1:
                    print("No available classes.")
                    continue  

                # Filter classes assigned to the teacher
                teacher_classes = [cls for cls in classes if cls[2] == teacher_id]

                if not teacher_classes:
                    print("No classes assigned to you.")
                    continue  

                # Extract class IDs assigned to the teacher
                class_ids = [cls[0] for cls in teacher_classes]
                print("Your Classes:", class_ids)

                # Ask teacher to enter class ID
                class_id = input("Enter the class ID: ").strip()
                if class_id not in class_ids:
                    print("Invalid class ID or not assigned to you.")
                    continue  

                try:
                    # Open and read students.txt file
                    with open("students.txt", "r") as file:
                        lines = file.readlines()
                        students = [line.strip().split(",") for line in lines]

                    # Check if students exist
                    if len(students) <= 1:
                        print("No Available Students.")
                        continue  

                    # Extract student IDs
                    student_ids = [student[0] for student in students[1:]]
                    print("Students:", student_ids)
                except FileNotFoundError:
                    print("students.txt file not found.")
                    continue  

                # Ask teacher to enter student ID
                student_id = input("Enter Student ID: ").strip()
                if student_id not in student_ids:
                    print("Invalid Student ID.")
                    continue  

                try:
                    # Open and read courses.txt file
                    with open("courses.txt", "r") as file:
                        lines = file.readlines()
                        courses = [line.strip().split(",") for line in lines]

                    # Check if courses exist
                    if len(courses) <= 1:
                        print("No Available Courses.")
                        continue  

                    # Extract course IDs
                    course_ids = [course[0] for course in courses[1:]]
                    print("Courses:", course_ids)
                except FileNotFoundError:
                    print("courses.txt file not found.")
                    continue  

                # Ask teacher to enter course ID
                course_id = input("Enter Course ID: ").strip()
                if course_id not in course_ids:
                    print("Invalid Course ID.")
                    continue  

                # Determine the type of assessment (Assignment or Exam)
                assessment_type = "Assignment" if choice == "1" else "Exam"

                # Ask for grade and feedback
                grade = input("Enter Grade: ").strip()
                feedback = input("Enter Your Feedback: ").strip()

                # Generate new assignment ID
                assignment_id = libraries.generate_new_id("assessments.txt", "ASM")

                try:
                    # Append grading information to assessments.txt file
                    with open("assessments.txt", "a") as file:
                        file.write(f"{assignment_id},{course_id},{class_id},{student_id},{assessment_type},{grade},{feedback}\n")
                    print("Graded Successfully")
                    return  
                except FileNotFoundError:
                    print("assessments.txt file not found.")
                    continue  
            except FileNotFoundError:
                print("classes.txt not found.")
                continue  

        elif choice == "3":  # If the user chooses to provide feedback
            # Generate a new feedback ID
            feedback_id = libraries.generate_new_id("feedbacks.txt", "FB")

            # Ask for student ID and target ID
            student_id = input("Enter Student ID (e.g., S001): ").strip()
            target_id = input("Enter Target ID (e.g., T001 for teacher or C001 for course): ").strip()
            feedback = input("Enter Your Feedback: ").strip()

            # Prepare the feedback record
            new_feedback = f"{feedback_id},{student_id},{target_id},{feedback}\n"

            try:
                # Append the feedback to feedbacks.txt file
                with open("feedbacks.txt", "a") as file:
                    file.write(new_feedback)
                print("Feedback Submitted Successfully")
                return  
            except FileNotFoundError:
                print("feedbacks.txt file not found.")
                continue  

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            return  
