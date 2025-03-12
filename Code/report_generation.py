def report_generation():
    def generate_performance_report():
        """ Generate academic performance report for all students """
        try:
            # Store student_id and student_name into students dictionary
            students = {}
            with open("../../Data/students.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    student_id = data[0]
                    student_name = data[1]
                    students[student_id] = student_name

            # Read assessments and process data
            report = {}
            with open("../../Data/assessments.txt", "r") as file:
                file.readline()  # Skip header

                for line in file:
                    if not line.strip():
                        continue

                    split_line = line.strip().split(",")
                    assessment_id, course_id, class_id, student_id, assessment_type, grade = split_line[:6]
                    grade = float(grade)

                    if student_id not in report:
                        report[student_id] = {
                            "name": students.get(student_id, "Unknown"),
                            "courses": {},
                            "total_grade": 0.0,
                            "course_count": 0,
                        }

                    # Store assignment and exam grades separately
                    if course_id not in report[student_id]["courses"]:
                        report[student_id]["courses"][course_id] = {"assignment": None, "exam": None}

                    if assessment_type.lower() == "assignment":
                        report[student_id]["courses"][course_id]["assignment"] = grade
                    elif assessment_type.lower() == "exam":
                        report[student_id]["courses"][course_id]["exam"] = grade

            # Calculate overall grades
            for student_id, student_data in report.items():
                for course_id, grades in student_data["courses"].items():
                    assignment_grade = grades.get("assignment", 0.0) or 0.0  # Set to 0.0 if it is None
                    exam_grade = grades.get("exam", 0.0) or 0.0
                    overall_grade = round((assignment_grade + exam_grade) / 2, 2) # Calculate the overall grade

                    student_data["total_grade"] += overall_grade
                    student_data["course_count"] += 1
                    grades["overall"] = overall_grade  # Store computed grade

            # Print out the Report
            print("\n" + "=" * 63)
            print(" " * 17 + "Academic Performance Report")
            print("=" * 63)

            for student_id, student_data in report.items():
                total_grade = student_data["total_grade"]
                course_count = student_data["course_count"]

                if course_count > 0:
                    cgpa = round(total_grade / course_count, 2)
                else:
                    cgpa = 0.0

                print(f"ID: {student_id:<10} Name: {student_data['name']:<20} CGPA: {cgpa:<5}")
                print("-" * 63)
                print(f"| {'Course ID':<12} | {'Assignment Grade':<18} | {'Exam Grade':<10} | {'Grade':<10} |")
                print("-" * 63)

                # Display courses and grades
                for course_id, grades in student_data["courses"].items():
                    print(
                        f"| {course_id:<12} | {grades['assignment'] if grades['assignment'] is not None else 'N/A':<18} "
                        f"| {grades['exam'] if grades['exam'] is not None else 'N/A':<10} | {grades['overall']:<10} |"
                    )
                print("-" * 63)
                print()

            print("=" * 63)

        except FileNotFoundError:
            print("❌ Error: assessment.txt or students.txt file not found.")
        except Exception as e:
            print(f"⚠️ Error: Unable to generate academic performance report. Details: {e}")

    def class_attendance_report():
        try:
            class_attendance = {} # Store attendance data

            with open("../../Data/attendances.txt", "r") as file:
                # Skip header
                file.readline()

                # Store data in class_attendance dictionary
                for line in file:
                    attendance_id, class_id, student_id, data,status = line.strip().split(",")

                    if class_id not in class_attendance:
                        class_attendance[class_id] = {"present": 0, "absent": 0}

                    if status == "Present":
                        class_attendance[class_id]["present"] += 1
                    elif status == "Absent":
                        class_attendance[class_id]["absent"] += 1

            # Display attendance report
            print("\n" + "=" * 60)
            print(" " * 14 + "Class Attendance Report")
            print("=" * 60)
            print(f"| {'Class ID':<12} | {'Present':<10} | {'Absent':<10} | {'Attendance (%)':<15} |")
            print("-" * 60)

            for class_id, data in class_attendance.items():
                total = data["present"] + data["absent"]
                attendance_percentage = (data["present"] / total) * 100 if total > 0 else 0
                print(f"| {class_id:<12} | {data['present']:<10} | {data['absent']:<10} | {attendance_percentage:<15.2f} |")
            print("=" * 60)

        except FileNotFoundError:
            print("❌ Error: attendances.txt file not found.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred. Details: {e}")

    def student_attendance_report():
        try:
            students_name = {} # Store students data
            with open("../../Data/students.txt", "r") as file:
                # Skip header
                file.readline()
                for line in file:
                    student_id, student_name, *others = line.strip().split(",")
                    students_name[student_id] = student_name

            students_attendance = {} # Store students attendance
            with open("../../Data/attendances.txt", "r") as file:
                # Skip header
                file.readline()

                for line in file:
                    attendance_id, class_id, student_id, date, status = line.strip().split(",")
                    if student_id not in students_attendance:
                        students_attendance[student_id] = {
                            "total_classes": 0,
                            "total_classes_attended": 0
                        }

                    students_attendance[student_id]["total_classes"] += 1
                    if status == "Present":
                        students_attendance[student_id]["total_classes_attended"] += 1

            # Display the Student Attendance Report
            print("\n" + "=" * 94)
            print(" " * 32 + "Student Attendance Report")
            print("=" * 94)
            print(f"| {'Student ID':<12} | {'Name':<20} | {'Total Classes':<15} | {'Classes Attended':<15} | {'Attendance (%)':<15} |")
            print("-" * 94)

            for student_id in students_attendance:
                total_classes = students_attendance[student_id]["total_classes"]
                attended_classes = students_attendance[student_id]["total_classes_attended"]

                # Calculate attendance percentage safely
                if total_classes > 0:
                    attendance_percentage = round((attended_classes / total_classes) * 100, 2)
                else:
                    attendance_percentage = 0.00

                student_name = students_name.get(student_id, "Unknown")


                print(f"| {student_id:<12} | {student_name:<20} | {total_classes:<15} | {attended_classes:<16} | {attendance_percentage:<15} |")

            print("=" * 94)


        except FileNotFoundError:
            print("❌ Error: attendances.txt file not found.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred. Details: {e}")

    def generate_students_financial_report():
        """ Generate financial report for all students """
        try:
            students_name = {}  # Store students' names
            with open("../../Data/students.txt", "r") as file:
                file.readline()  # Skip header
                for line in file:
                    data = line.strip().split(",")
                    if len(data) >= 2:
                        student_id, student_name = data[:2]
                        students_name[student_id.strip()] = student_name.strip()

            print("\nFinancial Report")
            print("=" * 105)
            print(
                f"| {'Student ID':<12} | {'Name':<20} | {'Total Fees':<12} | {'Fees Paid':<10} | {'Amount Left':<11} | {'Completion of Payment':<20} |")
            print("-" * 105)

            with open("../../Data/students_finance.txt", "r") as file:
                file.readline()  # Skip header
                for line in file:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue

                    data = line.split(",")
                    if len(data) < 3:
                        print(f"⚠️ Skipping invalid line: {line}")
                        continue

                    student_id, total_fees, fees_paid = data[:3]
                    student_id = student_id.strip()
                    total_fees, fees_paid = int(total_fees), int(fees_paid) # Change string to integer

                    amount_left = total_fees - fees_paid
                    if amount_left == 0:
                        pay = "Completed"
                    else:
                        pay = "Not Completed"

                    student_name = students_name.get(student_id, "Unknown")
                    print(f"| {student_id:<12} | {student_name:<20} | {total_fees:<12} | {fees_paid:<10} | {amount_left:<11} | {pay:<21} |")

            print("=" * 105)

        except FileNotFoundError:
            print("❌ Error: students_finance.txt file not found.")
        except Exception as e:
            print(f"⚠️ Error: Unable to generate financial report. Details: {e}")

    def generate_institution_financial_report():
        """
        Generate financial report for the institution.
        """
        try:
            revenues = []
            expenses = []
            total_amount_revenue = 0
            total_amount_expenses = 0

            with open("../../Data/institution_finance.txt", "r") as file:
                file.readline()  # Skip the header line

                for line in file:
                    finance = line.strip().split(",")
                    if len(finance) == 4:
                        # Collect revenues and expenses
                        revenues.append((finance[0], int(finance[1])))
                        expenses.append((finance[2], int(finance[3])))

            # Print Revenue Section Report
            print("\n" + "=" * 70)
            print(" " * 24 + "Institution Financial Report")
            print("=" * 70)
            print("Revenue Details:")
            print("-" * 70)
            print(f"| {'Name':<48} | {'Amount (RM)':<15} |")
            print("-" * 70)

            for name_revenue, amount in revenues:
                print(f"| {name_revenue:<48} | {amount:<15,} |")
                total_amount_revenue += amount

            print("-" * 70)
            print(f"Total Revenue: USD {total_amount_revenue:,}")
            print("=" * 70)

            # Print Expense Section
            print("\nExpense Details:")
            print("-" * 70)
            print(f"| {'Name':<48} | {'Amount (RMD)':<15} |")
            print("-" * 70)

            for name_expense, amount in expenses:
                print(f"| {name_expense:<48} | {amount:<15,} |")  # Format with commas
                total_amount_expenses += amount

            print("-" * 70)
            print(f"Total Expenses: RM {total_amount_expenses:,}")
            print("=" * 70)

            # Print Net Profit/Loss Report
            net_profit = total_amount_revenue - total_amount_expenses
            print(f"\nNet Profit/Loss: RM {net_profit:,}")
            print("=" * 70)

        except FileNotFoundError:
            print("❌ Error: institution_finance.txt file not found.")
        except Exception as e:
            print(f"⚠️ Error: Unable to generate financial report. Details: {e}")

    while True:
        try:
            print("\n" + "=" * 50)
            print("              REPORT GENERATION MENU              ")
            print("=" * 50)
            print("1. Academic Performance Report")
            print("2. Class Attendance Report")
            print("3. Student Attendance Report")
            print("4. Financial Report for Students")
            print("5. Financial Report for Institution")
            print("6. Back")
            print("=" * 50)

            choice = int(input("👉 Choose your option by number: "))
            print("=" * 50)

            if choice == 1:
                generate_performance_report()
            elif choice == 2:
                class_attendance_report()
            elif choice == 3:
                student_attendance_report()
            elif choice == 4:
                generate_students_financial_report()
            elif choice == 5:
                generate_institution_financial_report()
            elif choice == 6:
                print("Exiting Report Generation Menu. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please choose a valid number (1-6).")

        except ValueError:
            print("❌ Please enter a valid number (1-6).")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred. Details: {e}")

# report_generation()