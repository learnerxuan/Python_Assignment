def student_management():
    def view_record():
        """ View student record """
        try:
            def view_student_personal_details():
                """ View students personal details from students.txt amd record.txt """
                try:
                    # Store all data from students.txt to students dictionary
                    students = {}
                    with open("../../Data/students.txt", "r") as file:
                        # Skip header
                        file.readline()

                        for line in file:
                            data = line.strip().split(",")
                            student_id = data[0]
                            students[student_id] = {
                                "name": data[1],
                                "password": data[2],
                                "phone_number": data[3],
                                "email": data[4],
                                "gender": data[5],
                                "school_enrollment_status": data[6],
                                "parent_id": data[7]
                            }

                    print("\n" + "=" * 150)
                    print(f"| {'ID':<10} | {'Name':<20} | {'Password':<15} | {'Phone Number':<15} | {'Email':<27} | {'Gender':<10} | {'Enrollment Status':<18} | {'Parent ID':<10} |")
                    print("-" * 150)

                    # Print all student records
                    for student_id, student in students.items():
                        print(f"| {student_id:<10} | {student['name']:<20} | {student['password']:<15} | {student['phone_number']:<15} | {student['email']:<27} | {student['gender']:<10} | {student['school_enrollment_status']:<18} | {student['parent_id']:<10} |")

                    # with open("../../Data/record.txt", "r") as file:
                    #     # Skip header
                    #     file.readline()
                    #     for line in file:
                    #         data = line.strip().split(", ")
                    #         student_id, enrollment_status = data
                    #
                    #         # Retrieve student details from students dictionary
                    #         student = students.get(student_id)
                    #         print(
                    #             f"| {student_id:<5} | {student['name']:<20} | {student['password']:<15} | {student['phone_number']:<15} | {student['email']:<25} | {student['gender']:<10} | {enrollment_status:<17} | {student['parent_id']:<10}")

                    print("=" * 150)

                except FileNotFoundError as e:
                    print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
                except Exception as e:
                    print(f"⚠️ Error: Unable to display student records. Details: {e}")

            def view_academic_performance():
                """ View academic performance of students """
                try:
                    print("Viewing Academic Performance : ")
                    print("\n" + "=" * 151)
                    print(
                        f"| {'Assessment ID':<15} | {'Course ID':<10} | {'Course Name':<30} | {'Class ID':<15} | {'Student ID':<15} | {'Student Name':<15} | {'Assessment Type':<15} | {'Grade':<10} |")
                    print("-" * 151)

                    students = {}
                    with open("../../Data/students.txt") as file:
                        # Skip header
                        file.readline()

                        for line in file:
                            data = line.strip().split(",")
                            student_id = data[0]
                            students[student_id] = data[1]

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
                            if len(data) < 7:
                                continue  # Skip invalid lines
                            assessment_id, course_id, class_id, student_id, assessment_type, grade, assess_feedback = data
                            student_name = students.get(student_id, "Unknown")
                            course_name = courses.get(course_id, "Unknown")
                            print(
                                f"| {assessment_id:<15} | {course_id:<10} | {course_name:<30} | {class_id:<15} | {student_id:<15} | {student_name:<15} | {assessment_type:<15} | {grade:<10} |")

                    print("=" * 151)
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

                # with open("../../Data/students.txt", "r") as file:
                #     for line in file:
                #         all_lines = line.strip().split(",")
                #         if all_lines[0] == id:
                #             found = True
                #             print(f"Updating record for user ID: {id}")
                #             new_name = input("Enter new name (or press Enter to keep the current name): ").strip() or all_lines[1]
                #             new_password = input("Enter new password (or press Enter to keep the current password): ").strip() or all_lines[2]
                #             new_phone_number = input("Enter new phone number (or press Enter to keep the current phone number): ").strip() or all_lines[3]
                #             new_email = input("Enter new email (or press Enter to keep the current email): ").strip() or all_lines[4]
                #
                #             # Handle gender input
                #             gender_input = input(
                #                 "Enter gender (0 - Male, 1 - Female) (or press Enter to keep the current gender): ").strip()
                #             if gender_input == "":
                #                 gender = all_lines[5]  # Keep the current gender
                #             elif gender_input == "0":
                #                 gender = "Male"
                #             elif gender_input == "1":
                #                 gender = "Female"
                #             else:
                #                 print("Invalid gender input. Keeping the current gender.")
                #                 gender = all_lines[5]
                #
                #             # Add the updated record
                #             updated_records.append(
                #                 f"{all_lines[0]},{new_name},{new_password},{new_phone_number},{new_email},{gender}\n")
                #         else:
                #             updated_records.append(line)

                with open("../../Data/students.txt","r") as file:
                    for line in file:
                        all_lines = line.strip().split(",")
                        if all_lines[0] == id:
                            found = True
                            new_school_enrollment_status = str(input("Enter new school enrollment status (or press Enter to keep the current school enrollment status): "))
                            new_parent_id = str(input("Enter new parent id (or press Enter to keep the current parent id): "))
                            updated_records.append(f"{all_lines[0]},{all_lines[1]},{all_lines[2]},{all_lines[3]},{all_lines[4]},{all_lines[5]},{new_school_enrollment_status},{new_parent_id}")
                        else:
                            updated_records.append(line)
                if not found:
                    print(f"User with ID '{id}' not found. Please try again.")
                    return

                # Write updated records back to the file
                with open("../../Data/students.txt", "w") as file:
                    file.writelines(updated_records)

                print(f"User ID: {id} record updated successfully!")

            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")

        def update_student_academic_performance():
            try:
                id = str(input("Enter assessment ID to be updated : ")).strip()
                found = False

                updated_records = []

                with open("../../Data/assessments.txt","r") as file:
                    for line in file:
                        all_lines = line.strip().split(",")
                        if id == all_lines[0]:
                            found = True
                            new_grade = str(input("Enter new grade: "))
                            updated_records.append(f"{all_lines[0]},{all_lines[1]},{all_lines[2]},{all_lines[3]},{all_lines[4]},{new_grade},{all_lines[6]}")
                        else:
                            updated_records.append(line)

                if not found:
                    print(f"User with ID '{id}' not found. Please try again.")
                    return

                # Write updated records back to the file
                with open("../../Data/assessments.txt", "w") as file:
                    file.writelines(updated_records)

                print(f"Assessment ID: {id} record updated successfully!")

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

student_management()