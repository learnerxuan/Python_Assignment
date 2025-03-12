def generate_report(teacher_id):
    print(f"Generating Report on Student Performance and Participation for Teacher ID: {teacher_id}...")
    print("1)Student Performance Report")
    print("2)Attendance Report")

    choice=input("Enter Your Choice:").strip()
    if choice == "1":
        try:
            # Read classes data
            with open("classes.txt", "r") as file:
                classes = [line.strip().split(",") for line in file.readlines()]

            # Read assessments data
            with open("assessments.txt", "r") as file:
                assessments = [line.strip().split(",") for line in file.readlines()]

            # Read feedback data
            with open("feedbacks.txt", "r") as file:
                feedback = [line.strip().split(",") for line in file.readlines()]

        except FileNotFoundError:
            print(f"Txt File not found.")
            return

        # Filter classes taught by the teacher
        teacher_classes = [cls[0] for cls in classes if len(cls) >= 3 and cls[2] == teacher_id]

        if not teacher_classes:
            print(f"No classes found for Teacher ID: {teacher_id}.")
            return

        # Create a dictionary to store student performance and participation
        student_reports = {}

        # Process assessments for the teacher's classes
        for assessment in assessments:
            if len(assessment) < 7:  # Ensure the assessment record is valid
                continue

            class_id = assessment[2]
            if class_id not in teacher_classes:  # Skip assessments for other teachers' classes
                continue

            student_id = assessment[3]
            assessment_type = assessment[4]
            grade = assessment[5]
            assess_feedback = assessment[6]

            if student_id not in student_reports:
                student_reports[student_id] = {"classes": {},"feedback": []}

            if class_id not in student_reports[student_id]["classes"]:
                student_reports[student_id]["classes"][class_id] = {"assignments": [],"exams": []}

            if assessment_type == "assignment":
                student_reports[student_id]["classes"][class_id]["assignments"].append((grade, assess_feedback))
            elif assessment_type == "exam":
                student_reports[student_id]["classes"][class_id]["exams"].append((grade, assess_feedback))

        # Process feedback for the teacher's classes
        for fb in feedback:
            if len(fb) < 4:  # Ensure the feedback record is valid
                continue

            student_id = fb[1]
            feedback_text = fb[3]

            if student_id in student_reports:
                student_reports[student_id]["feedback"].append(feedback_text)

        # Generate the report
        report = f"Student Performance and Participation Report for Teacher ID: {teacher_id}\n"
        report += "=" * 70 + "\n"

        for student_id, data in student_reports.items():
            report += f"\nStudent ID: {student_id}\n"
            report += "-" * 70 + "\n"

            for class_id, class_data in data["classes"].items():
                report += f"Class ID: {class_id}\n"
                report += "  Assignments:\n"
                for grade, feedback in class_data["assignments"]:
                    report += f"    Grade: {grade}, Feedback: {feedback}\n"
                report += "  Exams:\n"
                for grade, feedback in class_data["exams"]:
                    report += f"    Grade: {grade}, Feedback: {feedback}\n"

            report += f"Feedback:\n"
            for fb in data["feedback"]:
                report += f"  - {fb}\n"
            report += "\n"

        # Display the report to the console
        print(report)
        print("Report generation complete.")

    if choice == "2":
        try:
            # Read classes data
            with open("classes.txt", "r") as file:
                classes = [line.strip().split(",") for line in file.readlines()]

            # Read attendance data from "attendances.txt"
            with open("attendances.txt", "r") as file:
                attendance_records = [line.strip().split(",") for line in file.readlines()]

        except FileNotFoundError:
            print("Error: One or more required files not found (classes.txt or attendances.txt).")
            return

        # Filter classes assigned to the teacher
        teacher_classes = [cls[0] for cls in classes if len(cls) >= 3 and cls[2] == teacher_id]

        if not teacher_classes:
            print(f"No classes found for Teacher ID: {teacher_id}.")
            return

        # Dictionary to store attendance data for students
        student_attendance = {}

        # Process attendance records
        for record in attendance_records:
            if len(record) < 5:  # Ensure the attendance record is valid
                continue

            attendance_id, class_id, student_id, date, status = record

            if class_id not in teacher_classes:
                continue  # Skip attendance records for other classes

            if student_id not in student_attendance:
                student_attendance[student_id] = []

            student_attendance[student_id].append((class_id, date, status))

        # Generate attendance report
        report = f"Attendance Report for Teacher ID: {teacher_id}\n"
        report += "=" * 70 + "\n"

        for student_id, records in student_attendance.items():
            report += f"\nStudent ID: {student_id}\n"
            report += "-" * 70 + "\n"

            for class_id, date, status in records:
                report += f"Class ID: {class_id} | Date: {date} | Status: {status}\n"

        # Display the report
        print(report)
        print("Attendance report generation complete.")