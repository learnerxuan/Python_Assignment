def course_management():
    def view_courses():
        """ Display all courses in a formatted table."""
        try:
            # Open the courses.txt file and read the records
            with open("../../Data/courses.txt", "r") as file:
                # Read the first line (header)
                header = file.readline().strip().split(",")

                # Print the table header
                print("=" * 140)
                print(f"| {'Course Code':<12} | {'Course Name':<30} | {'Description':<40} | {'Teacher ID':<45} |")
                print("-" * 140)

                # Print each course record
                for line in file:
                    course = line.strip().split(",")
                    if len(course) == 4:
                        print(f"| {course[0]:<12} | {course[1]:<30} | {course[2]:<40} | {course[3]:<45} |")

                print("=" * 140)
        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to read student records. Details: {e}")

    def add_course():
        print("Adding new course...")
        try:
            while True:
                course_id = str(input("Enter course ID (or type 'exit' to cancel): ")).strip()

                if course_id.lower() == "exit":
                    return

                # Check if the course already exists
                course_exists = False
                with open("../../Data/courses.txt", "r") as file:
                    for line in file:
                        check_exist = line.strip().split(",")[0]
                        if check_exist == course_id:
                            course_exists = True
                            break

                if not course_exists:
                    break
                else:
                    print(f"Error : Course with ID {course_id} already exists. Please reenter different course ID. ")

            course_name = str(input("Enter course name: ")).strip()
            description = str(input("Enter course description: ")).strip()

            print("Enter teacher IDs one by one. Press 'Enter' (empty input) to finish.")
            teacher_ids = []

            # Check if the teacher's ID exists
            while True:
                teacher_id = str(input("Enter teacher's id: ")).strip()
                if not teacher_id:
                    break

                teacher_found = False
                with open("../../Data/teachers.txt", "r") as file:
                    for line in file:
                        check_exist = line.strip().split(",")[0]
                        if check_exist == teacher_id:
                            teacher_found = True
                            break

                if teacher_found:
                    teacher_ids.append(teacher_id)
                else:
                    print(f"❌ Teacher's ID {teacher_id} does not exist")

            if not teacher_ids:
                print("⚠️ No valid teacher IDs entered. Course addition canceled.")
                return

            # Append the new course to courses.txt
            with open("../../Data/courses.txt", "a+") as file:
                file.seek(0)  # Move to the beginning of the file
                content = file.read()
                if content and not content.endswith("\n"):  # Ensure file ends with a newline
                    file.write("\n")
                file.write(f"{course_id},{course_name},{description},{' '.join(teacher_ids)}\n")  # Add a newline at the end
            print(f"✅ New course added successfully!")

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to process the request. Details: {e}")

    def update_course():
        try:
            print("Updating course ...")

            while True:
                course_id = str(input("Enter Course ID to update (or type 'exit' to cancel): ")).strip()

                if course_id.lower() == "exit":
                    return

                found = False
                course_data = []
                teacher_data = {}

                # Load all teacher data
                with open("../../Data/teachers.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        teacher_data[data[0]] = data[1]  # {teacher_id: teacher_name}

                # Read courses.txt and check if course exists
                with open("../../Data/courses.txt", "r") as file:
                    for line in file:
                        course = line.strip().split(",")

                        if course[0] == course_id:
                            found = True
                            new_course_name = str(
                                input("Enter new course name (or press Enter to keep current name): ")).strip() or \
                                              course[1]
                            new_description = str(input(
                                "Enter new description (or press Enter to keep current description): ")).strip() or \
                                              course[2]

                            # Extract current teachers
                            current_teachers = course[3].split()

                            # Display current teachers
                            print("=" * 45)
                            print(f"| {'Teacher ID':<15} | {'Teacher Name':<23} |")
                            print("-" * 45)
                            for teacher in current_teachers:
                                print(f"| {teacher:<15} | {teacher_data.get(teacher, 'Unknown'):<23} |")
                            print("=" * 45)

                            # Remove teachers
                            while True:
                                remove_teacher = str(
                                    input("Enter Teacher ID to remove (or press Enter to skip): ")).strip()
                                if not remove_teacher:
                                    break
                                if remove_teacher in current_teachers:
                                    current_teachers.remove(remove_teacher)
                                    print(f"✅ Removed {remove_teacher}.")
                                else:
                                    print(f"⚠️ Teacher ID '{remove_teacher}' not found.")

                            # Add new teachers
                            print("Enter new teacher IDs one by one. Press 'Enter' (empty input) to finish.")
                            while True:
                                new_teacher_id = str(input("Enter new Teacher ID: ")).strip()
                                if not new_teacher_id:
                                    break
                                if new_teacher_id in teacher_data:
                                    if new_teacher_id not in current_teachers:
                                        current_teachers.append(new_teacher_id)
                                        print(f"✅ Added {new_teacher_id}.")
                                    else:
                                        print(f"⚠️ Teacher ID '{new_teacher_id}' is already assigned.")
                                else:
                                    print(f"❌ Teacher ID '{new_teacher_id}' does not exist.")

                            # Prevent saving a course with no teachers
                            if not current_teachers:
                                print("⚠️ A course must have at least one teacher assigned.")
                                return

                            # Store updated course info
                            updated_course = f"{course_id},{new_course_name},{new_description},{' '.join(current_teachers)}"
                            course_data.append(updated_course)

                        else:
                            course_data.append(line.strip())

                if not found:
                    print(f"❌ Course '{course_id}' not found. Please enter a valid course ID.")
                    continue

                # Write updated course data
                with open("../../Data/courses.txt", "w") as file:
                    file.write("\n".join(course_data) + "\n")

                print("✅ Course record updated successfully!")
                return

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to process the request. Details: {e}")

    def delete_course():
        try:
            while True:
                print("Deleting course...")
                found = False
                new_record = []
                target_course = str(input("Enter course ID of the course to be deleted: ")).strip()

                with open("../../Data/courses.txt") as file:
                    for line in file:
                        if target_course == line.strip().split(",")[0]:
                            found = True
                            print(f"✅ Course ID '{target_course}' is deleted.")
                        else:
                            new_record.append(line)

                if not found:
                    print(f"❌ Course ID '{target_course}' not found")
                else:
                    with open("../../Data/courses.txt", "w") as file:
                        file.writelines(new_record)
                    return

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

course_management()