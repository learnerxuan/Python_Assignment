def administrator():
    def system_administration():
        def add_user():
            """ Add New User for Admin, Teacher, Staff, and Student """
            while True:  # Loop to redisplay the Add User menu
                try:
                    print("\n==================================================")
                    print("                  USER MANAGEMENT                 ")
                    print("==================================================")
                    print("1. Add User for Admin")
                    print("2. Add User for Teacher")
                    print("3. Add User for Staff")
                    print("4. Add User for Student")
                    print("5. Back")
                    print("==================================================")

                    choice = int(input("👉 Choose your option by number: "))

                    if choice == 1:
                        user = "admin"
                    elif choice == 2:
                        user = "teacher"
                    elif choice == 3:
                        user = "staff"
                    elif choice == 4:
                        user = "student"
                    elif choice == 5:
                        # Exit the Add User menu
                        break
                    else:
                        print("Invalid choice. Please choose again.")
                        continue

                    print("\n==================================================")
                    print(f"                 ADD {user.upper()} USER                  ")
                    print("==================================================")

                    # Take input from user and store it in variables
                    id = str(input("Enter id: "))
                    name = str(input("Enter name: "))
                    password = str(input("Enter password: "))
                    phone_number = str(input("Enter phone number: "))
                    email = str(input("Enter email: "))
                    gender_option = int(input("Enter gender (0 - Male, 1 - Female): "))
                    if gender_option == 0:
                        gender = "Male"
                    elif gender_option == 1:
                        gender = "Female"
                    else:
                        print("Invalid gender choice. Please try again.")
                        continue

                    print("--------------------------------------------------")
                    print(f" Success! {user.upper()} user has been added.")
                    print("==================================================\n")

                    # Save all variables into the respective file
                    file_path = f"../Data/{user}.txt"
                    with open(file_path, "a+") as file:
                        file.seek(0)  # Move the cursor to the beginning of the file
                        content = file.read()
                        if content and not content.endswith("\n"):  # Ensure no extra blank lines
                            file.write("\n")
                        file.write(f"{id},{name},{password},{phone_number},{email},{gender}")
                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")
                except Exception as e:
                    print(f"⚠️ An unexpected error occurred: {e}")

        def update_user():
            """Update user by inputting user id"""
            while True:  # Loop to redisplay the update menu
                try:
                    print("\n==================================================")
                    print("                  USER MANAGEMENT                 ")
                    print("==================================================")
                    print("1. Update Admin User")
                    print("2. Update Teacher User")
                    print("3. Update Staff User")
                    print("4. Update Student User")
                    print("5. Back")
                    print("==================================================")

                    choice = int(input("👉 Choose your option by number: "))

                    if choice == 1:
                        user = "admin"
                    elif choice == 2:
                        user = "teacher"
                    elif choice == 3:
                        user = "staff"
                    elif choice == 4:
                        user = "student"
                    elif choice == 5:
                        # Exit the update user menu
                        break
                    else:
                        print("Invalid choice. Please choose again.")
                        continue

                    id = str(input("Enter id to update: ")).strip()
                    found = False
                    updated_records = []
                    file_path = f"../Data/{user}.txt"

                    # Read and process the file
                    with open(file_path, "r") as file:
                        for line in file:
                            all_lines = line.strip().split(",")
                            if all_lines[0] == id:
                                found = True
                                print(f"Updating record for user ID: {id}")
                                new_name = input(
                                    "Enter new name (or press Enter to keep the current name): ").strip() or all_lines[
                                               1]
                                new_password = input(
                                    "Enter new password (or press Enter to keep the current password): ").strip() or \
                                               all_lines[2]
                                new_phone_number = input(
                                    "Enter new phone number (or press Enter to keep the current phone number): ").strip() or \
                                                   all_lines[3]
                                new_email = input(
                                    "Enter new email (or press Enter to keep the current email): ").strip() or \
                                            all_lines[4]

                                # Handle gender input
                                gender_input = input(
                                    "Enter gender (0 - Male, 1 - Female) (or press Enter to keep the current gender): ").strip()
                                if gender_input == "":
                                    gender = all_lines[5]  # Keep the current gender
                                elif gender_input == "0":
                                    gender = "Male"
                                elif gender_input == "1":
                                    gender = "Female"
                                else:
                                    print("Invalid gender input. Keeping the current gender.")
                                    gender = all_lines[5]

                                # Add the updated record
                                updated_records.append(
                                    f"{all_lines[0]},{new_name},{new_password},{new_phone_number},{new_email},{gender}\n")
                            else:
                                updated_records.append(line)

                    if not found:
                        print(f"User with ID '{id}' not found. Please try again.")
                        continue  # Redisplay the update menu

                    # Write updated records back to the file
                    with open(file_path, "w") as file:
                        file.writelines(updated_records)

                    print(f"User ID: {id} record updated successfully!")

                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")
                except Exception as e:
                    print(f"⚠️ An unexpected error occurred: {e}")

        def delete_user():
            while True:  # Loop to stay within the delete user menu
                try:
                    print("\n==================================================")
                    print("                  USER MANAGEMENT                 ")
                    print("==================================================")
                    print("1. Delete Admin User")
                    print("2. Delete Teacher User")
                    print("3. Delete Staff User")
                    print("4. Delete Student User")
                    print("5. Back")
                    print("==================================================")

                    choice = int(input("👉 Choose your option by number: "))

                    if choice == 1:
                        user = "admin"
                    elif choice == 2:
                        user = "teacher"
                    elif choice == 3:
                        user = "staff"
                    elif choice == 4:
                        user = "student"
                    elif choice == 5:
                        break
                    else:
                        print("Invalid choice. Please choose again.")
                        continue

                    found = False
                    new_record = []
                    target_user_id = str(input("Enter user id to be deleted: ")).strip()
                    file_path = f"../Data/{user}.txt"

                    with open(file_path) as file:
                        for line in file:
                            if target_user_id == line.strip().split(",")[0]:
                                found = True
                                print(f"Record of id '{target_user_id}' is deleted.")
                            else:
                                new_record.append(line)

                    if not found:
                        print(f"Id '{target_user_id}' not found. Please try again.")
                        continue  # Redisplay the delete user menu

                    with open(file_path, "w") as file:
                        file.writelines(new_record)

                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")
                except Exception as e:
                    print(f"⚠️ An unexpected error occurred: {e}")

        """System Administration Menu"""
        while True:
            print("\n" + "=" * 50)
            print("                SYSTEM ADMINISTRATION               ")
            print("=" * 50)
            print("1. Add User")
            print("2. Update User")
            print("3. Delete User")
            print("4. Back")
            print("=" * 50)

            try:
                user_choice = int(input("👉 Choose your option by number: "))
                print("=" * 50)  # Separator after input for clean output

                if user_choice == 1:
                    print("\n➡️ Redirecting to Add User...")
                    add_user()
                elif user_choice == 2:
                    print("\n➡️ Redirecting to Update User...")
                    update_user()
                elif user_choice == 3:
                    print("\n➡️ Redirecting to Delete User...")
                    delete_user()
                elif user_choice == 4:
                    print("\n🔙 Returning to the previous menu...")
                    return
                else:
                    print("❌ Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")

    def student_management():

        def view_record():
            """ View student record """
            try:
                def view_student_personal_details():
                    """ View students personal details from student.txt amd record.txt """
                    try:
                        # Store all data from student.txt to students dictionary
                        students = {}
                        with open("../Data/student.txt", "r") as file:
                            # Skip header
                            file.readline()

                            for line in file:
                                data = line.strip().split(", ")
                                student_id = data[0]
                                students[student_id] = {
                                    "name": data[1],
                                    "password": data[2],
                                    "phone_number": data[3],
                                    "email": data[4],
                                    "gender": data[5],
                                }

                        print("\n" + "=" * 129)
                        print(f"| {'ID':<5} | {'Name':<20} | {'Password':<15} | {'Phone Number':<15} | {'Email':<25} | {'Gender':<10} | {'Enrollment Status':<15} |")
                        print("-" * 129)

                        with open("../Data/record.txt", "r") as file:
                            # Skip header
                            file.readline()
                            for line in file:
                                data = line.strip().split(", ")
                                student_id, enrollment_status = data

                                # Retrieve student details from students dictionary
                                student = students.get(student_id)
                                print(f"| {student_id:<5} | {student['name']:<20} | {student['password']:<15} | {student['phone_number']:<15} | {student['email']:<25} | {student['gender']:<10} | {enrollment_status:<17} |")

                        print("=" * 129)

                    except FileNotFoundError as e:
                        print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
                    except Exception as e:
                        print(f"⚠️ Error: Unable to display student records. Details: {e}")

                def view_academic_performance():
                    """ View academic performance of students """
                    try:
                        print("Viewing Academic Performance : ")
                        print("\n" + "=" * 87)
                        print(f"| {'ID':<5} | {'Name':<20} | {'Course ID':<15} | {'Assignment Grade':<15} | {'Exam Grade':<15} |")
                        print("-" * 87)

                        with open("../Data/student.txt") as file:
                            # Skip header
                            file.readline()

                            students = {}
                            for line in file:
                                data = line.strip().split(", ")
                                student_id = data[0]
                                students[student_id] = data[1]

                        with open("../Data/academic_performance.txt","r") as file:
                            # Skip header
                            file.readline()

                            for line in file:
                                data = line.strip().split(",")
                                student_id,course_id,assignment_grade,exam_grade = data
                                student_name = students.get(student_id, "Unknown")
                                print(f"| {student_id:<5} | {student_name:<20} | {course_id:<15} | {assignment_grade:<16} | {exam_grade:<15} | ")

                        print("=" * 87)
                    except FileNotFoundError as e:
                        print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
                    except Exception as e:
                        print(f"⚠️ Error: Unable to display student records. Details: {e}")

                while True:
                    print("\n" + "=" * 50)
                    print("              STUDENT RECORD MENU              ")
                    print("=" * 50)
                    print("1. View Personal Details")
                    print("2. View Academic Performance")
                    print("3. Back")
                    print("=" * 50)

                    try:
                        choice = int(input("👉 Choose your option by number: "))
                        print("=" * 50)

                        if choice == 1:
                            view_student_personal_details()
                        elif choice == 2:
                            view_academic_performance()
                        elif choice == 3:
                            break
                        else:
                            print("❌ Invalid choice. Please choose a valid number (1-3).")
                    except ValueError:
                        print("❌ Invalid input. Please enter a valid number (1-3).")

            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to read student records. Details: {e}")

        def update_record():
            """ Update students record, either personal details or academic performance """

            def update_student_personal_details():
                try:
                    id = str(input("Enter id to update: ")).strip()
                    found = False
                    updated_records = []

                    with open("../Data/student.txt", "r") as file:
                        for line in file:
                            all_lines = line.strip().split(",")
                            if all_lines[0] == id:
                                found = True
                                print(f"Updating record for user ID: {id}")
                                new_name = input(
                                    "Enter new name (or press Enter to keep the current name): ").strip() or all_lines[
                                               1]
                                new_password = input(
                                    "Enter new password (or press Enter to keep the current password): ").strip() or \
                                               all_lines[2]
                                new_phone_number = input(
                                    "Enter new phone number (or press Enter to keep the current phone number): ").strip() or \
                                                   all_lines[3]
                                new_email = input(
                                    "Enter new email (or press Enter to keep the current email): ").strip() or \
                                            all_lines[4]

                                # Handle gender input
                                gender_input = input(
                                    "Enter gender (0 - Male, 1 - Female) (or press Enter to keep the current gender): ").strip()
                                if gender_input == "":
                                    gender = all_lines[5]  # Keep the current gender
                                elif gender_input == "0":
                                    gender = "Male"
                                elif gender_input == "1":
                                    gender = "Female"
                                else:
                                    print("Invalid gender input. Keeping the current gender.")
                                    gender = all_lines[5]

                                # Add the updated record
                                updated_records.append(
                                    f"{all_lines[0]},{new_name},{new_password},{new_phone_number},{new_email},{gender}\n")
                            else:
                                updated_records.append(line)

                    records = []
                    with open("../Data/record.txt", "r") as file:
                        for line in file:
                            all_lines = line.strip().split(",")
                            if all_lines[0] == id:
                                found = True
                                new_enrollment_status = input(
                                    "Enter enrollment status (or press Enter to keep the current enrollment status): ").strip() or \
                                           all_lines[
                                               1]
                                records.append(f"{all_lines[0]},{new_enrollment_status}\n")
                            else:
                                records.append(line)

                    if not found:
                        print(f"User with ID '{id}' not found. Please try again.")
                        return

                    # Write updated records back to the file
                    with open("../Data/student.txt", "w") as file:
                        file.writelines(updated_records)

                    with open("../Data/record.txt", "w") as file:
                        file.writelines(records)

                    print(f"User ID: {id} record updated successfully!")

                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")
                except Exception as e:
                    print(f"⚠️ An unexpected error occurred: {e}")

            def update_student_academic_performance():
                try:
                    id = str(input("Enter id of the student to update it's academic performance : ")).strip()
                    found = False

                    student_data = {}
                    all_records = []

                    with open("../Data/academic_performance.txt","r") as file:
                        # Skip header
                        header = file.readline()
                        all_records.append(header)

                        for line in file:
                            student_id, course_id, assignment_grade, exam_grade = line.strip().split(",")
                            all_records.append(line.strip())
                            if student_id == id:
                                found = True
                                if student_id not in student_data:
                                    student_data[student_id] = {}
                                student_data[student_id][course_id] = {
                                    "assignment_grade":assignment_grade,
                                    "exam_grade":exam_grade
                                }
                        # print(student_data)
                        # print(student_data[id].items())

                    if not found:
                        print(f"❌ Student with ID '{id}' not found. Please try again.")
                        return

                    print(f"Current Academic Performance of student id: {id} ")
                    print("=" * 64)
                    print(f"| {'ID':<5} | {'Course ID':<15} | {'Assignment Grade':<15} | {'Exam Grade':<15} |")
                    print("-" * 64)
                    for course_id,grades in student_data[id].items():
                        print(f"| {id:<5} | {course_id:<15} | {grades['assignment_grade']:<16} | {grades['exam_grade']:<15} | ")
                    print("=" * 64 )


                    targeted_course_id = str(input("Enter the course id to be updated : ")).strip()
                    # print(student_data[id])
                    if targeted_course_id not in student_data[id]:
                        print(f"❌ Course ID '{targeted_course_id}' not found for student ID '{id}'. Please try again.")
                        return

                    new_assignment_grade = str(input("Enter new assignment grade ( or press Enter to keep the current assignment grade ) : ")) or student_data[id][targeted_course_id]["assignment_grade"]
                    new_exam_grade = str(input("Enter new exam grade ( or press Enter to keep the current exam grade ) : ")) or student_data[id][targeted_course_id]["exam_grade"]
                    student_data[id][targeted_course_id]["assignment_grade"] = new_assignment_grade
                    student_data[id][targeted_course_id]["exam_grade"] = new_exam_grade

                    with open("../Data/academic_performance.txt","w") as file:
                        file.write(header)
                        for record in all_records[1:]:
                            record_data = record.split(",")
                            student_id, course_id = record_data[0], record_data[1]
                            if student_id == id and course_id == targeted_course_id:
                                file.write(f"{id},{course_id},{new_assignment_grade},{new_exam_grade}\n")
                            else:
                                file.write(record + "\n")

                    print(f"✅ Academic performance for student ID '{id}' and course ID '{targeted_course_id}' updated successfully!")

                except FileNotFoundError:
                    print("❌ Error: academic_performance.txt file not found. Please ensure the file exists.")
                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")
                except Exception as e:
                    print(f"⚠️ An unexpected error occurred: {e}")

            while True:
                print("\n" + "=" * 50)
                print("              STUDENT RECORD MENU              ")
                print("=" * 50)
                print("1. Update Personal Details")
                print("2. Update Academic Performance")
                print("3. Back")
                print("=" * 50)

                try:
                    choice = int(input("👉 Choose your option by number: "))
                    print("=" * 50)

                    if choice == 1:
                        update_student_personal_details()
                    elif choice == 2:
                        update_student_academic_performance()
                    elif choice == 3:
                        break
                    else:
                        print("❌ Invalid choice. Please choose a valid number (1-3).")
                except ValueError:
                    print("❌ Invalid input. Please enter a valid number (1-3).")

        while True:
            try:
                print("\n" + "=" * 50)
                print("               STUDENT MANAGEMENT MENU               ")
                print("=" * 50)
                print("1. View Student Records")
                print("2. Update Student Record")
                print("3. Back")
                print("=" * 50)

                user_choice = int(input("👉 Choose your option by number: "))
                print("=" * 50)  # Separator for better readability

                if user_choice == 1:
                    view_record()
                elif user_choice == 2:
                    update_record()
                elif user_choice == 3:
                    break
                else:
                    print("❌ Invalid choice. Please choose a valid number (1-3).")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number (1-3).")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred. Details: {e}")

    def course_management():

        def view_courses():
            """ Display all courses in a formatted table."""
            try:
                # Open the courses.txt file and read the records
                with open("../Data/courses.txt", "r") as file:
                    # Read the first line (header)
                    header = file.readline().strip().split(",")

                    # Print the table header
                    print("=" * 105)
                    print(f"| {'Course Code':<12} | {'Course Name':<30} | {'Description':<40} | {'Teacher ID':<10} |")
                    print("-" * 105)

                    # Print each course record
                    for line in file:
                        course = line.strip().split(",")
                        if len(course) == 4:
                            print(f"| {course[0]:<12} | {course[1]:<30} | {course[2]:<40} | {course[3]:<10} |")

                    print("=" * 105)
            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to read student records. Details: {e}")

        def add_course():
            print("Adding new course...")
            try:
                course_code = str(input("Enter course code: ")).strip()

                # Check if the course already exists
                with open("../Data/courses.txt", "r") as file:
                    for line in file:
                        check_exist = line.strip().split(",")[0]
                        if check_exist == course_code:
                            print(f"Error : Course with code {course_code} already exists")
                            return

                course_name = str(input("Enter course name: ")).strip()
                description = str(input("Enter course description: ")).strip()

                # Check if the teacher's ID exists
                found = False
                teacher_id = str(input("Enter teacher's id: ")).strip()
                with open("../Data/teacher.txt", "r") as file:
                    for line in file:
                        check_exist = line.strip().split(",")[0]
                        if check_exist == teacher_id:
                            found = True

                if not found:
                    print(f"❌ Teacher's ID {teacher_id} does not exist")
                    return

                # Append the new course to courses.txt
                with open("../Data/courses.txt", "a+") as file:
                    file.seek(0)  # Move to the beginning of the file
                    content = file.read()
                    if content and not content.endswith("\n"):  # Ensure file ends with a newline
                        file.write("\n")
                    file.write(f"{course_code},{course_name},{description},{teacher_id}\n")  # Add a newline at the end
                print(f"✅ New course added successfully!")

            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to process the request. Details: {e}")

        def update_course():
            try:
                print("Updating course ...")
                course_code = str(input("Enter Course Code to update: ")).strip()
                found = False
                course_record = []
                with open("../Data/courses.txt", "r") as file:
                    for line in file:
                        all_lines = line.strip().split(",")
                        if all_lines[0] == course_code:
                            found = True
                            new_course_name = str(
                                input("Enter new course name (or press Enter to keep the current name): ")).strip() or \
                                       all_lines[1]
                            new_description = str(
                                input("Enter new description (or press Enter to keep the current description): ")).strip() or \
                                        all_lines[2]
                            course_record.append(
                                f"{all_lines[0]},{new_course_name},{new_description},{new_description},{all_lines[3]}\n")

                        else:
                            course_record.append(line)

                if not found:
                    print(f"❌ Course: {course_code} not found")
                    return

                with open("../Data/courses.txt", "w") as file:
                    file.writelines(course_record)
                print("✅ Course record updated successfully!")

            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to process the request. Details: {e}")

        def delete_course():
            try:
                print("Deleting course...")
                found = False
                new_record = []
                target_course = str(input("Enter course code of the course to be deleted: ")).strip()

                with open("../Data/courses.txt") as file:
                    for line in file:
                        if target_course == line.strip().split(",")[0]:
                            found = True
                            print(f"✅ Record of username '{target_course}' is deleted.")
                        else:
                            new_record.append(line)

                if not found:
                    print(f"❌ Course code '{target_course}' not found")
                    return

                with open("../Data/courses.txt", "w") as file:
                    file.writelines(new_record)

            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to process the request. Details: {e}")

        while True:
            try:
                print("\n" + "=" * 50)
                print("              COURSE MANAGEMENT MENU              ")
                print("=" * 50)
                print("1. View All Courses")
                print("2. Add Course")
                print("3. Update Course")
                print("4. Delete Course")
                print("5. Back")
                print("=" * 50)

                user_choice = int(input("👉 Choose your option by number: "))
                print("=" * 50)

                if user_choice == 1:

                    view_courses()
                elif user_choice == 2:
                    add_course()
                elif user_choice == 3:
                    update_course()
                elif user_choice == 4:
                    delete_course()
                elif user_choice == 5:
                    break
                else:
                    print("❌ Invalid choice. Please choose a valid number (1-5).")
            except ValueError:
                print("❌ Please enter a valid number (1-5).")

    def class_schedule():

        def view_class_schedule():
            """ Display class schedule in a formatted table """
            try:
                # Open the courses.txt file and read the records
                with open("../Data/schedule.txt", "r") as file:
                    # Print the table header
                    print("=" * 85)
                    print(f"| {'Course ID':<12} | {'Day':<10} | {'Starting Time':<10} | {'Ending Time':<10} | {'Class':<10} | {'Teacher ID':<10} |")
                    print("-" * 85)

                    # Skip header
                    header = file.readline()

                    # Print each course record
                    for line in file:
                        class_schedule = line.strip().split(",")
                        print(f"| {class_schedule[0]:<12} | {class_schedule[1]:<10} | {class_schedule[2]:<13} | {class_schedule[3]:<11} |{class_schedule[4]:<10}  | {class_schedule[5]:<10} |")

                    print("=" * 85)
            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to process the request. Details: {e}")

        def add_class_schedule():
            print("Adding new class...")
            try:
                course_code = str(input("Enter course code: ")).strip()
                # Check whether course code exist
                course_found = False
                teacher_for_course = None
                with open("../Data/courses.txt", "r") as file:
                    for line in file:
                        check_exist = line.strip().split(",")
                        if course_code == check_exist[0]:
                            course_found = True
                            teacher_for_course = check_exist[3]  # The teacher's ID for this course
                            break

                if not course_found:
                    print(f"❌ Course code: {course_code} not found")
                    return

                day = str(input("Enter day (e.g., Monday): ")).strip()
                start_time = str(input("Enter start time (HH:MM): ")).strip()
                end_time = str(input("Enter end time (HH:MM): ")).strip()
                room = str(input("Enter room number: ")).strip()

                teacher_id = str(input("Enter teacher's id: ")).strip()
                #Check whether instructor exist
                teacher_found = False
                with open("../Data/teacher.txt", "r") as file:
                    for line in file:
                        check_exist = line.strip().split(",")
                        if teacher_id == check_exist[0]:
                            teacher_found = True
                            break

                if not teacher_found:
                    print(f"❌ Teacher ID: {teacher_id} not found")
                    return

                if teacher_id != teacher_for_course:
                    print(f"❌ Error: Teacher ID '{teacher_id}' is not assigned to teach course '{course_code}'.")
                    return

                with open("../Data/schedule.txt","r") as file:
                    for line in file:
                        check_exist = line.strip().split(",")

                        scheduled_day, scheduled_start, scheduled_end, scheduled_room, scheduled_instructor = (
                            check_exist[1],
                            check_exist[2],
                            check_exist[3],
                            check_exist[4],
                            check_exist[5],
                        )

                        # Room conflict
                        if scheduled_day == day and scheduled_room == room:
                            if end_time > scheduled_start and start_time < scheduled_end:
                                print("❌ Conflict detected: The room is already reserved for that time.")
                                return

                        # Teacher conflict
                        if scheduled_day == day and scheduled_instructor == teacher_id:
                            if end_time > scheduled_start and start_time < scheduled_end:
                                print(f"❌ Conflict detected: Instructor {teacher_id} is busy at that time.")
                                return

                with open("../Data/schedule.txt", "a") as file:
                    file.write(f"{course_code},{day},{start_time},{end_time},{room},{teacher_id}\n")
                print(f"✅ New schedule for course '{course_code}' added successfully!")

            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to add new schedule. Details: {e}")

        def update_class_schedule():
            """
            Update class schedule for a specific course code.
            - If there are multiple class for the specific course code, user will be asked to select one to update.
            - If only one class for the specific course code, user can directly update it.
            """
            try:
                print("Updating class schedule ...")
                course_code = str(input("Enter Course Code to update: ")).strip() # Input course code which user wanted update
                found = False
                schedules = []  # Store all rows from the file
                matching_schedules = []  # Store rows matching the course code

                # Check if the course code exist, and store data in respective list.
                with open("../Data/schedule.txt", "r") as file:
                    for line in file:
                        class_schedule = line.strip().split(",")
                        schedules.append(class_schedule)
                        if course_code == class_schedule[0]:
                            found = True
                            matching_schedules.append(class_schedule)
                if not found:
                    print(f"❌ Course code '{course_code}' not found.")
                    return

                # Display matching schedules in a table
                print("\nCurrent schedule(s) for course code:", course_code)
                print("=" * 85)
                print(
                    f"{'No.':<3}| {'Course Code':<12} | {'Day':<10} | {'Start Time':<10} | {'End Time':<10} | {'Room':<10} | {'Instructor':<10} |")
                print("-" * 85)

                for idx, schedule in enumerate(matching_schedules, start=1):
                    print(
                        f"{idx:<3}| {schedule[0]:<12} | {schedule[1]:<10} | {schedule[2]:<10} | {schedule[3]:<10} | {schedule[4]:<10} | {schedule[5]:<10} |")
                print("=" * 85)

                # Check whether there are multiple class for this course code
                if len(matching_schedules) == 1:
                    selected_schedule = matching_schedules[0]
                else:
                    while True:
                        try:
                            row_number = int(input("Enter the row number to update: "))
                            if 1 <= row_number <= len(matching_schedules):
                                selected_schedule = matching_schedules[row_number - 1]
                                break
                            else:
                                print(f"Invalid input. Please enter a number between 1 and {len(matching_schedules)}.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")

                # User update data for this course code schedule
                print("\nUpdating the selected schedule...")
                new_day = input(f"Enter new day (or press Enter to keep '{selected_schedule[1]}'): ").strip() or \
                          selected_schedule[1]
                new_start_time = input(
                    f"Enter new start time (or press Enter to keep '{selected_schedule[2]}'): ").strip() or \
                                 selected_schedule[2]
                new_end_time = input(
                    f"Enter new end time (or press Enter to keep '{selected_schedule[3]}'): ").strip() or \
                               selected_schedule[3]
                new_room = input(f"Enter new room (or press Enter to keep '{selected_schedule[4]}'): ").strip() or \
                           selected_schedule[4]

                # Update the selected schedule in the main list (schedule of all course code)
                for schedule in schedules:
                    if schedule == selected_schedule:
                        schedule[1] = new_day
                        schedule[2] = new_start_time
                        schedule[3] = new_end_time
                        schedule[4] = new_room


                # Write the updated schedules back to the file
                with open("../Data/schedule.txt", "w") as file:
                    for schedule in schedules:
                        file.write(",".join(schedule) + "\n")

                print(" ✅ Class schedule updated successfully!")


            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to add new schedule. Details: {e}")

        def delete_class_schedule():
            """ Delete a class schedule for a given course code """
            try:
                print("Deleting class...")
                found = False
                schedules = []
                matching_targeted_class = []
                new_record = []
                targeted_course_code = str(input("Enter course code of the class to be deleted: ")).strip()

                with open("../Data/schedule.txt", "r") as file:
                    for line in file:
                        class_schedule = line.strip().split(",")
                        schedules.append(class_schedule)
                        if class_schedule[0] == targeted_course_code:
                            found = True
                            matching_targeted_class.append(class_schedule)

                # Check if the course code was found
                if not found:
                    print(f"❌ Course code '{targeted_course_code}' not found.")
                    return

                if len(matching_targeted_class) == 1:
                    selected_course_code = matching_targeted_class[0]
                else:
                    print("\nCurrent schedule(s) for course code:", targeted_course_code)
                    print("=" * 85)
                    print(f"{'No.':<3}| {'Course Code':<12} | {'Day':<10} | {'Start Time':<10} | {'End Time':<10} | {'Room':<10} | {'Instructor':<10} |")
                    print("-" * 85)

                    for idx, schedule in enumerate(matching_targeted_class, start=1):
                        print(f"{idx:<3}| {schedule[0]:<12} | {schedule[1]:<10} | {schedule[2]:<10} | {schedule[3]:<10} | {schedule[4]:<10} | {schedule[5]:<10} |")
                    print("=" * 85)

                    while True:
                        try:
                            row_number = int(input("Enter row number to be deleted: "))
                            if 1 <= row_number <= len(matching_targeted_class):
                                selected_course_code = matching_targeted_class[row_number - 1]
                                break
                            else:
                                print(f"❌ Invalid input. Please enter a number between 1 and {len(matching_targeted_class)}.")
                        except ValueError:
                            print("❌ Invalid input. Please enter a valid number.")
                        except Exception as e:
                            print(f"⚠️ Error: Unable to add new schedule. Details: {e}")

                for schedule in schedules:
                    if schedule == selected_course_code:
                        print(f"✅ Class for course code : {targeted_course_code} deleted successfully!")
                    else:
                        new_record.append(schedule)

                    with open("../Data/schedule.txt","w") as file:
                        for line in new_record:
                            file.write(",".join(line) + "\n")


            except FileNotFoundError as e:
                print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
            except Exception as e:
                print(f"⚠️ Error: Unable to add new schedule. Details: {e}")

        while True:
            try:
                print("\n" + "=" * 50)
                print("         CLASS SCHEDULE MANAGEMENT MENU         ")
                print("=" * 50)
                print("1. View Schedule")
                print("2. Add Class")
                print("3. Update Class")
                print("4. Delete Class")
                print("5. Back")
                print("=" * 50)

                user_choice = int(input("👉 Choose your option by number: "))
                print("=" * 50)

                if user_choice == 1:
                    view_class_schedule()
                elif user_choice == 2:
                    add_class_schedule()
                elif user_choice == 3:
                    update_class_schedule()
                elif user_choice == 4:
                    delete_class_schedule()
                elif user_choice == 5:
                    break
                else:
                    print("❌ Invalid choice. Please choose a valid number (1-5).")
            except ValueError:
                print("❌ Please enter a valid number (1-5).")

    def report_generation():

        def generate_performance_report():
            """ Generate academic performance report for all students """
            try:
                students = {}
                with open("../Data/student.txt","r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        student_id = data[0]
                        student_name = data[1]
                        students[student_id] = student_name

                data = []
                with open("../Data/academic_performance.txt", "r") as file:
                    # Skip header
                    file.readline()

                    for line in file:
                        if not line.strip():
                            continue
                        split_line = line.strip().split(",")
                        if len(split_line) != 4:
                            print(f"Warning: Skipping invalid: {line.strip()}")
                            continue
                        data.append(split_line)

                # Generate report
                report = {}
                for info in data:
                    student_id, course_id, assignment_grade, exam_grade = info
                    assignment_grade = float(assignment_grade)
                    exam_grade = float(exam_grade)
                    overall_grade = round((assignment_grade + exam_grade)/2,2)

                    if student_id not in report:
                        report[student_id] = {
                            "name": students.get(student_id, "Unknown"),
                            "courses": [],
                            "total_grade": 0,
                            "course_count": 0,
                        }

                    report[student_id]["courses"].append({
                        "course_id": course_id,
                        "assignment_grade": assignment_grade,
                        "exam_grade": exam_grade,
                        "overall_grade": overall_grade,
                    })

                    report[student_id]["total_grade"] += overall_grade
                    report[student_id]["course_count"] += 1

                print("\n" + "=" * 63)
                print(" " * 17 + "Academic Performance Report")
                print("=" * 63)

                for student_id, student_data in report.items():
                    cgpa = round(student_data["total_grade"] / student_data["course_count"], 2)

                    # Display student header
                    print(f"ID: {student_id:<10} Name: {student_data['name']:<20} CGPA: {cgpa:<5}")
                    print("-" * 63)
                    print(f"| {'Course ID':<12} | {'Assignment Grade':<18} | {'Exam Grade':<10} | {'Grade':<10} |")
                    print("-" * 63)

                    # Display courses and grades
                    for course in student_data["courses"]:
                        print(f"| {course['course_id']:<12} | {course['assignment_grade']:<18} | {course['exam_grade']:<10} | {course['overall_grade']:<10} |")
                    print("-" * 63)
                    print()

                print("=" * 63)


            except FileNotFoundError:
                print("❌ Error: academic_performance.txt or student.txt file not found.")
            except Exception as e:
                print(f"⚠️ Error: Unable to generate academic performance report. Details: {e}")

        def course_attendance_report():
            try:
                course_attendance = {}

                with open("../Data/attendance.txt", "r") as file:
                    # Skip header
                    file.readline()
                    for line in file:
                        student_id, course_id, date, status = line.strip().split(",")

                        if course_id not in course_attendance:
                            course_attendance[course_id] = {"present": 0, "absent": 0}

                        if status == "Present":
                            course_attendance[course_id]["present"] += 1
                        elif status == "Absent":
                            course_attendance[course_id]["absent"] += 1

                print("\n" + "=" * 60)
                print(" " * 14 + "Course Attendance Report")
                print("=" * 60)
                print(f"| {'Course ID':<12} | {'Present':<10} | {'Absent':<10} | {'Attendance (%)':<15} |")
                print("-" * 60)

                for course_id, data in course_attendance.items():
                    total = data["present"] + data["absent"]
                    attendance_percentage = (data["present"] / total) * 100 if total > 0 else 0
                    print(f"| {course_id:<12} | {data['present']:<10} | {data['absent']:<10} | {attendance_percentage:<15.2f} |")
                print("=" * 60)

            except FileNotFoundError:
                print("❌ Error: attendance.txt file not found.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred. Details: {e}")

        def student_attendance_report():
                try:
                    students_name = {}
                    with open("../Data/student.txt","r") as file:
                        # Skip header
                        file.readline()
                        for line in file:
                            student_id, student_name, *others = line.strip().split(",")
                            students_name[student_id] = student_name

                    students_attendance = {}
                    with open("../Data/attendance.txt","r") as file:
                        # Skip header
                        file.readline()

                        for line in file:
                            student_id, course_id, date, status = line.strip().split(",")
                            if student_id not in students_attendance:
                                students_attendance[student_id] = {
                                    "total_classes":0,
                                    "total_classes_attended":0
                                }

                            students_attendance[student_id]["total_classes"] += 1
                            if status == "Present":
                                students_attendance[student_id]["total_classes_attended"] += 1

                    print("\n" + "=" * 94)
                    print(" " * 32 + "Student Attendance Report")
                    print("=" * 94)
                    print(f"| {'Student ID':<12} | {'Name':<20} | {'Total Classes':<15} | {'Classes Attended':<15} | {'Attendance (%)':<15} |")
                    print("-" * 94)

                    for student_id, data in students_attendance.items():
                        attendance_percentage = (data["total_classes_attended"] / data["total_classes"]) * 100 if data["total_classes"] > 0 else 0
                        student_name = students_name.get(student_id)
                        print(f"| {student_id:<12} | {student_name:<20} | {data["total_classes"]:<15} | {data["total_classes_attended"]:<16} | {attendance_percentage:<15} |")
                    print("=" * 94)

                except FileNotFoundError:
                    print("❌ Error: attendance.txt file not found.")
                except Exception as e:
                    print(f"⚠️ An unexpected error occurred. Details: {e}")

        def generate_students_financial_report():
            """ Generate financial report for all students """
            try:
                students_name = {}
                with open("../Data/student.txt", "r") as file:
                    # Skip header
                    file.readline()
                    for line in file:
                        student_id, student_name, *others = line.strip().split(",")
                        students_name[student_id] = student_name

                print("\nFinancial Report")
                print("=" * 105)
                print(f"| {'Student ID':<12} | {'Name':<20} | {'Total Fees':<12} | {'Fees Paid':<10} | {'Amount Left':<11} | {'Completion of Payment':<20} |")
                print("-" * 105)

                with open("../Data/students_finance.txt", "r") as file:
                    # Skip header
                    file.readline()

                    for line in file:
                        student_id, total_fees, fees_paid = line.strip().split(",")
                        amount_left = int(total_fees) - int(fees_paid)
                        if total_fees != fees_paid:
                            pay = "Not Completed"
                        else:
                            pay = "Completed"
                        student_name = students_name.get(student_id)
                        print(f"| {student_id:<12} | {student_name:<20} | {total_fees:<12} | {fees_paid:<10} | {amount_left:<11} | {pay:<21} |")

                print("=" * 105)
            except FileNotFoundError:
                print("Error: students_finance.txt file not found.")
            except Exception as e:
                print(f"Error: Unable to generate financial report. Details: {e}")

        def generate_institution_financial_report():
            """
            Generate financial report for the institution.
            """
            try:
                revenues = []
                expenses = []
                total_amount_revenue = 0
                total_amount_expenses = 0

                with open("../Data/institution_finance.txt", "r") as file:
                    header = file.readline()  # Skip the header line

                    for line in file:
                        finance = line.strip().split(",")
                        if len(finance) == 4:
                            # Collect revenues and expenses
                            revenues.append((finance[0], int(finance[1])))
                            expenses.append((finance[2], int(finance[3])))

                # Print Revenue Section
                print("\n" + "=" * 70)
                print(" " * 24 + "Institution Financial Report")
                print("=" * 70)
                print("Revenue Details:")
                print("-" * 70)
                print(f"| {'Name':<48} | {'Amount (RM)':<15} |")
                print("-" * 70)

                for name_revenue, amount in revenues:
                    print(f"| {name_revenue:<48} | {amount:<15,} |")  # Format with commas
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

                # Print Net Profit/Loss
                net_profit = total_amount_revenue - total_amount_expenses
                print(f"\nNet Profit/Loss: RM {net_profit:,}")
                print("=" * 70)

            except FileNotFoundError:
                print("Error: institution_finance.txt file not found.")
            except Exception as e:
                print(f"Error: Unable to generate financial report. Details: {e}")

        while True:
            try:
                print("\n" + "=" * 50)
                print("              REPORT GENERATION MENU              ")
                print("=" * 50)
                print("1. Academic Performance Report")
                print("2. Course Attendance Report")
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
                    course_attendance_report()

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

    def logout():
        return

    """
    Administrator menu for managing system functions.
    """
    while True:
        try:
            print("\n" + "=" * 73)
            print(" " * 22 + "Administrator Menu")
            print("=" * 73)
            print(f"| {'No.':<3} | {'Function':<26} | {'Description':<34} |")
            print("-" * 73)
            print(f"| 1   | System Administration      | Add, Update, Delete User           |")
            print(f"| 2   | Student Management         | View, Update Student Record        |")
            print(f"| 3   | Course Management          | View, Add, Update, Delete Course   |")
            print(f"| 4   | Class Schedule             | View, Add, Update Schedule         |")
            print(f"| 5   | Report Generation          | Performance, Attendance, Finance   |")
            print(f"| 6   | Logout                     | Return to Login Screen             |")
            print(f"| 7   | Exit                       | Exit the System                    |")
            print("=" * 73)

            admin_choice = int(input("👉 Choose your option by number: "))
            print("=" * 73)

            if admin_choice == 1:
                system_administration()
            elif admin_choice == 2:
                student_management()
            elif admin_choice == 3:
                course_management()
            elif admin_choice == 4:
                class_schedule()
            elif admin_choice == 5:
                report_generation()
            elif admin_choice == 6:
                print("Logging out...")
                return
            elif admin_choice == 7:
                print("Exiting the system. Goodbye! Have have nice day ,see you next time !")
                quit()
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


administrator()










