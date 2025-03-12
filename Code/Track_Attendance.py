# Import necessary libraries
import libraries  

def track_attendance(teacher_id):
    print("Track Attendance")
    print("1) Record Attendance")
    print("2) View Attendance")

    # Ask user to choose an option
    choice = input("Enter choice: ").strip()

    while True:
        if choice == "1":  # If the user chooses to record attendance
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
                teacher_classes = [cls for cls in classes[1:] if cls[2] == teacher_id]

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
                    # Open and read course_enrollments.txt file
                    with open("course_enrollments.txt", "r") as file:
                        lines = file.readlines()
                        enrollments = [line.strip().split(",") for line in lines]

                    # Check if students are enrolled in the class
                    if len(enrollments) <= 1:
                        print("No students enrolled in this class.")
                        continue  

                    # Get student IDs enrolled in the selected class
                    student_ids = [enrollment[2] for enrollment in enrollments if enrollment[1] == class_id]
                    print("Students in Class:", student_ids)
                except FileNotFoundError:
                    print("course_enrollments.txt file not found.")
                    continue  

                # Ask for attendance date
                date = input("Enter the date (YYYY-MM-DD): ").strip()

                # Loop through student IDs and ask for attendance status
                for student_id in student_ids:
                    status = input(f"Is {student_id} present? (yes/no): ").strip().lower()

                    # Convert input into standardized format
                    if status == "yes":
                        status = "present"
                    else:
                        status = "absent"

                    # Generate a new attendance ID
                    attendance_id = libraries.generate_new_id("attendances.txt", "ATT")

                    # Append attendance record to attendances.txt
                    with open("attendances.txt", "a") as file:
                        file.write(f"{attendance_id},{class_id},{student_id},{date},{status}\n")

                print("Attendance recorded successfully.")
                return  
            except FileNotFoundError:
                print("classes.txt file not found.")
                continue  

        elif choice == "2":  # If the user chooses to view attendance
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
                teacher_classes = [cls for cls in classes[1:] if cls[2] == teacher_id]

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
                    # Open and read attendances.txt file
                    with open("attendances.txt", "r") as file:
                        lines = file.readlines()
                        attendance_records = [line.strip().split(",") for line in lines]

                    # Check if attendance records exist
                    if not attendance_records:
                        print("No attendance records found.")
                        continue  

                    # Display attendance for the selected class
                    print(f"Attendance for Class {class_id}:")
                    for record in attendance_records:
                        if record[1] == class_id:  # Ensure class ID matches
                            print(f"Student: {record[2]}, Date: {record[3]}, Status: {record[4]}")
                except FileNotFoundError:
                    print("attendances.txt file not found.")
                    continue  

            except FileNotFoundError:
                print("classes.txt file not found.")
                continue  

        else:
            print("Invalid choice. Please select 1 or 2.")
            return  
