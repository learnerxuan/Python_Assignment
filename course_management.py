import libraries
def course_management():
    def view_courses():
        """
        Display all courses in a formatted table.
        """
        try:
            # Open the courses.txt file and read the records
            with open("../../Data/courses.txt", "r") as file:
                # Skip header
                file.readline()

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
        """
        Add new course, input course_name,description,teacher_id
        """
        print("Adding new course...")
        try:
            course_name = str(input("Enter course name: ")).strip()
            if course_name.lower() == "exit":
                return # Return back to the menu

            description = str(input("Enter course description: ")).strip()
            if description.lower() == "exit":
                return

            # Print out Teacher ID and Teacher's Name in table form
            print("=" * 39)
            print(f"| {'Teacher ID':<12} | {'Teacher Name':<20} |")
            print("-" * 39)
            with open("../../Data/teachers.txt","r") as file:
                # Skip header
                file.readline()

                for line in file:
                    teacher = line.strip().split(",")
                    teacher_id = teacher[0]
                    teacher_name = teacher[1]
                    print(f"| {teacher_id:<12} | {teacher_name:<20} |")

            print("=" * 39)

            # Allow multiple teachers to be entered one by one
            print("Enter teacher IDs one by one. Press 'Enter' (empty input) to finish.")
            teacher_ids = [] # Store all Teacher ID

            # Check if the teacher's ID exists
            while True:
                teacher_id = str(input("Enter teacher's id: ")).strip()
                if not teacher_id:
                    break # Empty input, break the loop
                if teacher_id.lower() == "exit":
                    return

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

            # Cancel the course addition when there is no teacher ID inputted
            if not teacher_ids:
                print("⚠️ No valid teacher IDs entered. Course addition canceled.")
                return

            # Append the new course to courses.txt
            course_id = libraries.generate_new_id("../../Data/courses.txt", "C")
            with open("../../Data/courses.txt", "a+") as file:
                file.seek(0)  # Move to the beginning of the file
                content = file.read()
                if content and not content.endswith("\n"):  # Ensure file ends with a newline
                    file.write("\n")
                file.write(f"{course_id},{course_name},{description},{' '.join(teacher_ids)}\n")  # Add a newline at the end
            print(f"✅ New course with ID '{course_id}' is added successfully!")

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to process the request. Details: {e}")

    def update_course():
        """
        Update Course
        """
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
                            new_course_name = str(input("Enter new course name (or press Enter to keep current name): ")).strip() or course[1]
                            if new_course_name.lower() == "exit":
                                return

                            new_description = str(input("Enter new description (or press Enter to keep current description): ")).strip() or course[2]
                            if new_description.lower() == "exit":
                                return

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
                                remove_teacher = str(input("Enter Teacher ID to remove (or press Enter to skip): ")).strip()
                                if not remove_teacher:
                                    break

                                if remove_teacher.lower() == "exit":
                                    return

                                if remove_teacher in current_teachers:
                                    current_teachers.remove(remove_teacher)
                                    print(f"✅ Removed {remove_teacher}.")
                                else:
                                    print(f"⚠️ Teacher ID '{remove_teacher}' not found.")

                            # Add new teachers
                            print("=" * 39)
                            print(f"| {'Teacher ID':<12} | {'Teacher Name':<20} |")
                            print("-" * 39)
                            with open("../../Data/teachers.txt", "r") as file:
                                # Skip header
                                file.readline()

                                for line in file:
                                    teacher = line.strip().split(",")
                                    teacher_id = teacher[0]
                                    teacher_name = teacher[1]
                                    print(f"| {teacher_id:<12} | {teacher_name:<20} |")

                            print("=" * 39)
                            print("Enter new teacher IDs one by one. Press 'Enter' (empty input) to finish.")
                            while True:
                                new_teacher_id = str(input("Enter new Teacher ID: ")).strip()
                                if not new_teacher_id:
                                    break

                                if new_teacher_id.lower() =="exit":
                                    return

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
                    continue # Let user to reenter

                # Write updated course data
                with open("../../Data/courses.txt", "w") as file:
                    file.write("\n".join(course_data) + "\n")

                print("✅ Course record updated successfully!")
                return # Return back to the menu

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to process the request. Details: {e}")

    def delete_course():
        """
        Delete Course
        """
        try:
            while True:
                print("Deleting course...")

                found = False
                new_record = [] # Store updated data

                target_course = str(input("Enter course ID of the course to be deleted (or type 'exit' to cancel): ")).strip()
                if target_course.lower() == "exit":
                    return # Return back to the menu

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
                    return # Return back to the menu

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to process the request. Details: {e}")

    while True:
        try:
            # Course Management Menu
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

# course_management()