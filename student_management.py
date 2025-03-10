def student_management():
    def view_student_personal_details():
        """ View students' personal details from students.txt and parents.txt """
        try:
            print("\n" + "=" * 240)
            print(f"| {'ID':<10} | {'Name':<20} | {'Password':<15} | {'Phone Number':<15} | {'Email':<30} | {'Gender':<10} | {'Enrollment Status':<18} | {'Parent ID':<10} | {'Name':<20} | {'Phone Number':<15} | {'Email':<30} | {'Gender':<10} |")
            print("-" * 240)

            students = {} # Store students data

            # Read student records
            with open("../../Data/students.txt", "r") as file:
                file.readline()  # Skip header
                for line in file:
                    data = line.strip().split(",")  # Ensure no space after comma
                    if len(data) < 8:
                        continue  # Skip invalid lines

                    student_id = data[0]
                    students[student_id] = {
                        "name": data[1],
                        "password": data[2],
                        "phone_number": data[3],
                        "email": data[4],
                        "gender": data[5],
                        "enrollment_status": data[6],
                        "parent_id": data[7]
                    }

            parents = {} # Store parents data
            with open("../../Data/parents.txt", "r") as file:
                file.readline()  # Skip header

                for line in file:
                    parent_data = line.strip().split(",")
                    if len(parent_data) < 6:
                        continue  # Skip invalid lines

                    parent_id = parent_data[0]
                    parents[parent_id] = {
                        "name": parent_data[2],
                        "phone_number": parent_data[3],
                        "email": parent_data[4],
                        "gender": parent_data[5]
                    }

            # Print student and parent details in table form
            for student_id, details in students.items():
                parent_id = details["parent_id"]
                parent_details = parents.get(parent_id,{"name": "N/A", "phone_number": "N/A", "email": "N/A", "gender": "N/A"})

                print(f"| {student_id:<10} | {details['name']:<20} | {details['password']:<15} | {details['phone_number']:<15} | {details['email']:<30} | {details['gender']:<10} | {details['enrollment_status']:<18} | {parent_id:<10} | {parent_details['name']:<20} | {parent_details['phone_number']:<15} | {parent_details['email']:<30} | {parent_details['gender']:<10} |")

            print("=" * 240)

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to display student records. Details: {e}")

    def view_academic_performance():
        """
        View academic performance of students
        """
        try:
            print("=" * 151)
            print(f"| {'Assessment ID':<15} | {'Course ID':<10} | {'Course Name':<30} | {'Class ID':<15} | {'Student ID':<15} | {'Student Name':<15} | {'Assessment Type':<15} | {'Grade':<10} |")
            print("-" * 151)

            # Store student_id and name into students dictionary
            students = {}
            with open("../../Data/students.txt") as file:
                # Skip header
                file.readline()

                for line in file:
                    data = line.strip().split(",")
                    student_id = data[0]
                    students[student_id] = data[1]

            # Store course id and course name into courses dictionary
            courses = {}
            with open("../../Data/courses.txt") as file:
                # Skip header
                file.readline()

                for line in file:
                    data = line.strip().split(",")
                    course_id = data[0]
                    courses[course_id] = data[1]

            with open("../../Data/assessments.txt", "r") as file:
                # Skip header
                file.readline()

                for line in file:
                    data = line.strip().split(",")
                    if len(data) < 6:
                        continue  # Skip invalid lines
                    assessment_id, course_id, class_id, student_id, assessment_type, grade = data[:6]
                    student_name = students.get(student_id, "Unknown") # Retrieve student name from students
                    course_name = courses.get(course_id, "Unknown") # Retrieve course name from courses
                    print(f"| {assessment_id:<15} | {course_id:<10} | {course_name:<30} | {class_id:<15} | {student_id:<15} | {student_name:<15} | {assessment_type:<15} | {grade:<10} |")

            print("=" * 151)
        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to display student records. Details: {e}")

    def update_student_personal_details():
        while True:  # Loop to redisplay the update menu
            try:
                # Input ID of the user to update
                while True:
                    id = input("Enter user ID to update (or type 'exit' to return): ").strip()
                    if id.lower() == "exit":
                        return  # Return back to User Management Menu

                    found = False
                    updated_records = [] # Store updated data


                    with open("../../Data/students.txt", "r") as file:
                        for line in file:
                            all_lines = line.strip().split(",")

                            # If ID is found, allow updates
                            if all_lines[0] == id:
                                found = True
                                print(f"Updating record for user ID: {id}")
                                new_name = input("Enter new name (or press Enter to keep current name): ").strip() or all_lines[1]
                                if new_name.lower() == "exit":
                                    return

                                new_password = input(
                                    "Enter new password (or press Enter to keep current password): ").strip() or all_lines[2]
                                if new_password.lower() == "exit":
                                    return

                                new_phone_number = input(
                                    "Enter new phone number (or press Enter to keep current phone number): ").strip() or all_lines[3]
                                if new_phone_number.lower() == "exit":
                                    return

                                new_email = input("Enter new email (or press Enter to keep current email): ").strip() or all_lines[4]
                                if new_email.lower() == "exit":
                                    return

                                # Update gender
                                while True:
                                    gender_input = input(
                                        "Enter gender (0 - Male, 1 - Female) (or press Enter to keep current gender): ").strip().lower()
                                    if gender_input == "exit":
                                        return
                                    elif gender_input == "":
                                        gender = all_lines[5]  # Keep current gender
                                        break
                                    elif gender_input == "0":
                                        gender = "Male"
                                        break
                                    elif gender_input == "1":
                                        gender = "Female"
                                        break
                                    else:
                                        print("❌ Invalid gender choice. Please try again.")

                                school_enrollment_status = input("Enter new school enrollment status (or press Enter to keep current school enrollment status): ").strip() or all_lines[6]
                                if school_enrollment_status.lower() == "exit":
                                    return

                                data = f"{id},{new_name},{new_password},{new_phone_number},{new_email},{gender},{school_enrollment_status},{all_lines[7]}"

                                updated_records.append(data + "\n")
                            else:
                                updated_records.append(line)

                    if not found:
                        print(f"❌ User with ID '{id}' not found. Please try again.")
                        continue  # Redisplay the update menu

                    # Write updated data back to the file
                    with open("../../Data/students.txt", "w") as file:
                        file.writelines(updated_records)

                    print(f"✅ User ID: {id} record updated successfully!")
                    return

            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")

    def update_student_parent_details():
        while True:  # Loop to redisplay the update menu
            try:
                # Input ID of the user to update
                while True:
                    id = input("Enter Parent ID to update (or type 'exit' to return): ").strip()
                    if id.lower() == "exit":
                        return  # Return back to User Management Menu

                    found = False
                    updated_records = [] # Store updated data


                    with open("../../Data/parents.txt", "r") as file:
                        for line in file:
                            all_lines = line.strip().split(",")

                            # If ID is found, allow updates
                            if all_lines[0] == id:
                                found = True
                                print(f"Updating record for user ID: {id}")
                                new_name = input("Enter new name (or press Enter to keep current name): ").strip() or all_lines[2]
                                if new_name.lower() == "exit":
                                    return

                                new_phone_number = input("Enter new phone number (or press Enter to keep current phone number): ").strip() or all_lines[3]
                                if new_phone_number.lower() == "exit":
                                    return

                                new_email = input("Enter new email (or press Enter to keep current email): ").strip() or all_lines[4]
                                if new_email.lower() == "exit":
                                    return

                                # Update gender
                                while True:
                                    gender_input = input(
                                        "Enter gender (0 - Male, 1 - Female) (or press Enter to keep current gender): ").strip().lower()
                                    if gender_input == "exit":
                                        return
                                    elif gender_input == "":
                                        gender = all_lines[5]  # Keep current gender
                                        break
                                    elif gender_input == "0":
                                        gender = "Male"
                                        break
                                    elif gender_input == "1":
                                        gender = "Female"
                                        break
                                    else:
                                        print("❌ Invalid gender choice. Please try again.")

                                data = f"{id},{all_lines[1]},{new_name},{new_phone_number},{new_email},{gender}"

                                updated_records.append(data + "\n")
                            else:
                                updated_records.append(line)

                    if not found:
                        print(f"❌ User with ID '{id}' not found. Please try again.")
                        continue  # Redisplay the update menu

                    # Write updated data back to the file
                    with open("../../Data/parents.txt", "w") as file:
                        file.writelines(updated_records)

                    print(f"✅ User ID: {id} record updated successfully!")
                    return

            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")

    def update_student_academic_performance():
        """
        Update students' grade
        """
        try:
            while True:
                id = input("Enter assessment ID to be updated (or type 'exit' to return): ").strip()
                if id.lower() == "exit":
                    return  # Return back to the menu

                found = False
                updated_records = []

                with open("../../Data/assessments.txt", "r") as file:
                    for line in file:
                        all_lines = line.strip().split(",")

                        if id == all_lines[0]:  # If assessment ID is found
                            found = True

                            # Loop for valid grade input
                            while True:
                                new_grade = input("Enter new grade (or type 'exit' to return): ").strip()
                                if new_grade.lower() == "exit":
                                    return
                                try:
                                    new_grade = float(new_grade)
                                    if 0.00 <= new_grade <= 4.00:  # Ensure grade is within 0-4 range
                                        break
                                    else:
                                        print("❌ Grade must be between 0.00 and 4.00. Please try again.")
                                except ValueError:
                                    print("❌ Invalid input. Please enter a valid grade (e.g., 3.75).")

                            updated_records.append(f"{all_lines[0]},{all_lines[1]},{all_lines[2]},{all_lines[3]},{all_lines[4]},{new_grade},{all_lines[6]}\n")
                        else:
                            updated_records.append(line)

                if not found:
                    print(f"❌ Assessment ID '{id}' not found. Please try again.")
                    continue  # Let user to reenter when ID not found

                # Write updated records back to the file
                with open("../../Data/assessments.txt", "w") as file:
                    file.writelines(updated_records)

                print(f"✅ Assessment ID: {id} record updated successfully!")
                return  # Exit after successful update

        except FileNotFoundError:
            print("❌ Error: assessments.txt file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

    while True:
        try:
            print("\n" + "=" * 50)
            print("               STUDENT MANAGEMENT MENU               ")
            print("=" * 50)
            print("1. View Student Records")
            print("2. View Student Academic Performance")
            print("3. Update Student Personal Details")
            print("4. Update Student Parent's details")
            print("5. Update Student Academic Performance")
            print("6. Back")
            print("=" * 50)

            user_choice = int(input("👉 Choose your option by number: "))
            print("=" * 50)
            if user_choice == 1:
                view_student_personal_details()
            elif user_choice == 2:
                view_academic_performance()
            elif user_choice == 3:
                update_student_personal_details()
            elif user_choice == 4:
                update_student_parent_details()
            elif user_choice == 5:
                update_student_academic_performance()
            elif user_choice == 6:
                break
            else:
                print("❌ Invalid choice. Please choose a valid number (1-3).")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number (1-3).")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred. Details: {e}")

# student_management()