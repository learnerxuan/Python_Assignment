# Import necessary libraries
import libraries


def manage_courses(teacher_id):
    print("Manage Classes")
    print("1) Update Class")
    print("2) Create a Class")

    # Ask user to choose an option
    choice = input("Enter your choice: ").strip()

    while True:
        if choice == "1":  # If user chooses to update a class
            try:
                # Open and read classes.txt file
                with open("../Data/classes.txt", "r") as file:
                    lines = file.readlines()

                    # Convert each line into a list, skipping empty lines
                    classes = [line.strip().split(",") for line in lines if line.strip()]

                # If there are no classes available
                if len(classes) <= 1:
                    print("No available classes.")
                    continue

                    # Filter classes assigned to the teacher
                teacher_classes = []
                for cls in classes:
                    if len(cls) >= 3 and cls[2] == teacher_id:  # Check if teacher_id matches
                        teacher_classes.append(cls)

                # If no classes are assigned to this teacher
                if not teacher_classes:
                    print("No classes assigned to you.")
                    return

                    # Display teacher's classes
                class_ids = [cls[0] for cls in teacher_classes]
                print("Your Classes:", class_ids)

            except FileNotFoundError:  # Handle missing file error
                print("classes.txt file not found.")
                continue

                # Ask the teacher which class to update
            class_id = input("Enter the class ID to update: ").strip()
            found = False
            updated_classes = []

            for cls in classes:
                # Check if the class belongs to the teacher
                if len(cls) >= 3 and cls[0] == class_id and cls[2] == teacher_id:
                    found = True
                    print("Updating class:", cls)

                    # Display update options
                    print("Choose what to update:")
                    print("1) Day")
                    print("2) Start Time")
                    print("3) End Time")
                    print("4) Location")
                    print("5) Lesson Plan")
                    print("6) Notes")
                    print("7) Announcement")

                    # Get user input for update choices
                    update_choices = input("Enter option number(s), separated by commas: ").strip().split(',')
                    update_choices = [c.strip() for c in update_choices]  # Remove extra spaces

                    # Validate input choices
                    valid_options = {"1", "2", "3", "4", "5", "6", "7"}
                    if not set(update_choices).issubset(valid_options):
                        print("Invalid choices. Please enter numbers between 1 and 7.")
                        return

                        # Update selected fields
                    if "1" in update_choices:
                        cls[3] = input("Enter new day: ").strip()
                    if "2" in update_choices:
                        cls[4] = input("Enter new start time (HH:MM): ").strip()
                    if "3" in update_choices:
                        cls[5] = input("Enter new end time (HH:MM): ").strip()
                    if "4" in update_choices:
                        cls[6] = input("Enter new location: ").strip()
                    if "5" in update_choices:
                        cls[7] = input("Enter new lesson plan: ").strip()
                    if "6" in update_choices:
                        cls[8] = input("Enter new notes: ").strip()
                    if "7" in update_choices:
                        cls[9] = input("Enter new announcement: ").strip()

                    # Store updated class information
                    updated_classes.append(",".join(cls) + "\n")
                else:
                    # Keep other classes unchanged
                    updated_classes.append(",".join(cls) + "\n")

            # If the class was found and updated, save the changes
            if found:
                with open("../Data/classes.txt", "w") as file:
                    file.writelines(updated_classes)
                print("Class updated successfully.")
                return
            else:
                print("Class Not Available or You Are Not Authorized to Update It.")
                continue

        elif choice == "2":  # If user chooses to create a class
            try:
                # Open and read courses.txt file
                with open("../Data/courses.txt", "r") as file:
                    lines = file.readlines()

                    # Convert each line into a list, skipping empty lines
                    courses = [line.strip().split(",") for line in lines if line.strip()]

                # If no courses are available
                if len(courses) <= 1:
                    print("Not available courses")
                    continue

                    # Filter courses assigned to the teacher
                teacher_courses = [course[0] for course in courses if
                                   len(course) >= 4 and teacher_id in course[3].split()]

                # If no courses are assigned to this teacher
                if not teacher_courses:
                    print("No courses assigned to you.")
                    return

                    # Display teacher's assigned courses
                print("Courses Assigned to You:")
                print("course_id:", ", ".join(teacher_courses))

            except FileNotFoundError:  # Handle missing file error
                print("Courses .txt file not exist")
                continue

                # Get new class details from the teacher
            print("Creating a new class")
            class_id = libraries.generate_new_id("classes.txt", "CLS")  # Generate a new class ID
            course_id = input("Enter Course ID: ").strip()
            day = input("Enter Day: ").strip()
            start_time = input("Enter Start Time (HH:MM): ").strip()
            end_time = input("Enter End Time (HH:MM): ").strip()
            location = input("Enter Location: ").strip()
            lesson_plan = input("Enter Lesson Plan: ").strip()
            notes = input("Enter Notes: ").strip()
            announcement = input("Enter Announcement: ").strip()

            # Format the new class entry
            new_class = f"{class_id},{course_id},{teacher_id},{day},{start_time},{end_time},{location},{lesson_plan},{notes},{announcement}\n"

            try:
                # Append the new class to the file
                with open("../Data/classes.txt", "a") as file:
                    file.write(new_class)
                print("Class created successfully.")
                return
            except FileNotFoundError:  # Handle missing file error
                print("classes.txt file not found.")
                continue

        else:  # Handle invalid menu choice
            print("Invalid choice.")
            return

