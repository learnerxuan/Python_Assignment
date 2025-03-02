import staff_lib
import color

def manage_timetable():
    """Display manage timetable menu and process user choices."""
    while True:
        print(f"{'=' * 17}{color.BOLD}{color.BLUE} MANAGE TIMETABLE {color.RESET}{'=' * 17}")
        print(f"""{" " * 15}{color.YELLOW}1.{color.RESET}  Assign Teacher
{" " * 15}{color.YELLOW}2.{color.RESET}  Update Timetable
{" " * 15}{color.YELLOW}0.{color.RESET}  Back""")
        print(f"{'=' * 52}")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2])

        if choice == 1:
            assign_teacher()  # Assign a teacher to a class
        elif choice == 2:
            update_timetable()  # Update timetable details
        elif choice == 0:
            return  # Exit function to return to staff menu


def assign_teacher():
    """Assign a teacher to a class while ensuring no schedule conflicts."""
    while True:
        try:
            # Read classes and filter those with no teacher assigned
            classes, header = staff_lib.read_csv_file("./Data/classes.txt")

            print(",".join(header[0:7]))  # Display class headers
            for cls in classes:
                if cls["teacher_id"] == "None":  # Only show unassigned classes
                    print(",".join(map(str, (list(cls.values())[:7]))))

            # Get user input for class ID
            class_id = input("Enter class ID (0 to cancel): ").strip()
            if class_id == "0":
                return  # Restart loop if user cancels

            class_found = False
            teacher_assigned = False  # Track if a change is made

            # Validate class ID and ensure no teacher is assigned
            if staff_lib.search_value("./Data/classes.txt", 0, class_id) and staff_lib.search_value("./Data/classes.txt", 0, class_id, 2) == "None":
                print(",".join(header[0:7]))
                for cls in classes:
                    if cls["class_id"] == class_id:
                        class_found = True
                        print(",".join(map(str, (list(cls.values())[:7]))))

                        # Get teachers for the course
                        course_id = cls["course_id"]
                        teachers = staff_lib.search_value("./Data/courses.txt", 0, course_id, 3).split()
                        
                        # Display available teachers
                        for teacher in teachers:
                            print(f"{teacher},{staff_lib.search_value('./Data/teachers.txt', 0, teacher, 1)}")

                        assigned_tch = input("Enter teacher ID (0 to cancel): ").strip()
                        if assigned_tch == "0":
                            continue  # Restart loop if user cancels

                        if assigned_tch in teachers:
                            # Check for schedule conflicts before assigning
                            if check_teacher_conflict(classes, assigned_tch, cls["day"], cls["start_time"], cls["end_time"]):
                                print("Teacher has a schedule conflict at this time. Choose another teacher.")
                                continue

                            cls["teacher_id"] = assigned_tch
                            teacher_assigned = True  # Mark change as made

                # Write changes only if a teacher was assigned
                if teacher_assigned:
                    with open("./Data/classes.txt", "w") as writer:
                        writer.write(",".join(header) + "\n")
                        for cls in classes:
                            writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in cls.values()) + "\n")
                    print("Successfully added teacher.")
                else:
                    print("No changes were made.")

            else:
                print("Invalid class ID.")
                continue            

        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Unable to read/write the file.")
        return


def check_teacher_conflict(classes, teacher_id, day, start_time, end_time):
    """Check if the teacher is assigned to another class at the same time."""
    start_min = time_to_minutes(start_time)
    end_min = time_to_minutes(end_time)

    for cls in classes:
        if cls["teacher_id"] == teacher_id and cls["day"] == day:
            other_start = time_to_minutes(cls["start_time"])
            other_end = time_to_minutes(cls["end_time"])

            # Check overlapping time slots
            if (other_start <= start_min < other_end) or (other_start < end_min <= other_end) or (start_min <= other_start and end_min >= other_end):
                return True  # Conflict detected
    return False  # No conflict


def time_to_minutes(time_str):
    """Convert 'HH:MM' formatted time string to total minutes."""
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def check_conflict(classes, class_id, day, start_time, end_time, location):
    """
    Ensure the new class schedule does not conflict with existing schedules.
    - Ensures no overlap for the same day & location.
    - Ignores the class being updated.
    """
    start_min = time_to_minutes(start_time)
    end_min = time_to_minutes(end_time)

    for other_cls in classes:
        if other_cls["class_id"] == class_id:
            continue  # Skip checking itself
        
        # Check if same day and location
        if other_cls["day"] == day and other_cls["location"] == location:
            other_start = time_to_minutes(other_cls["start_time"])
            other_end = time_to_minutes(other_cls["end_time"])

            # Detect time conflicts
            if (other_start <= start_min < other_end) or (other_start < end_min <= other_end) or (start_min <= other_start and end_min >= other_end) or (start_min == other_start and end_min == other_end):
                return True  # Conflict detected
    return False  # No conflict


def update_timetable():
    """Modify class schedule based on teacher's request."""
    while True:
        try:
            print("ALL CLASS")
            all_class, header = staff_lib.read_csv_file("./Data/classes.txt")
            print(",".join(header[0:7]))

            for cls in all_class:
                print(",".join(map(str, (list(cls.values())[:7]))))

            # Get user input for class ID
            class_id = input("Enter class ID (0 to cancel): ").strip()
            if class_id == "0":
                return
            
            # Validate class ID
            if not staff_lib.search_value("./Data/classes.txt", 0, class_id):
                print("Invalid class ID. Please try again.")
                continue
            
            while True:
                classes, header = staff_lib.read_csv_file("./Data/classes.txt")

                print(",".join(header[0:7]))
                for cls in classes:
                    if cls["class_id"] == class_id:
                        print(",".join(map(str, (list(cls.values())[:7]))))

                        print("\nOption:\n1. Change Day\n2. Change Time\n3. Change Location\n0. Back")
                        choice = staff_lib.choose([0, 1, 2, 3])
                        
                        if choice == 0:
                            return 
                        elif choice == 1:
                            updated_cls = change_day(cls, classes)
                        elif choice == 2:
                            updated_cls = change_time(cls, classes)
                        elif choice == 3:
                            updated_cls = change_location(cls, classes)
                        
                        # Update modified class
                        for i in range(len(classes)):
                            if classes[i]["class_id"] == class_id:
                                classes[i] = updated_cls
                                break  

                # Write to file only if changes were made
                if any(classes[i] != all_class[i] for i in range(len(classes))):
                    with open("./Data/classes.txt", "w") as writer:
                        writer.write(",".join(header) + "\n")
                        for cls in classes:
                            writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in cls.values()) + "\n")
                    print("Successfully Changed.")

        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Unable to read/write the file.")
        return
    

def change_day(old_cls, classes):
    """Change the class day while ensuring no conflicts."""

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    new_cls = old_cls.copy()  # Create a copy of the original class record to modify

    print(f"Option: {', '.join(days)}")  # Display available days to the user

    while True:
        new_day = input("Enter new day (0 to cancel): ").strip().title()  # Get user input for the new day
        if new_day == "0":
            return old_cls  # Return original record if the user cancels

        if new_day in days:
            # Check if the new day causes a scheduling conflict
            if check_conflict(classes, old_cls["class_id"], new_day, old_cls["start_time"], old_cls["end_time"], old_cls["location"]):
                print("Conflict detected. Please try again.")  # Notify user of conflict
                continue

            new_cls["day"] = new_day  # Update class day
            return new_cls  # Return updated record

        else:
            print("Invalid day. Please try again.")  # Handle invalid input


def change_time(old_cls, classes):
    """Change the class time while ensuring no conflicts."""

    new_cls = old_cls.copy()  # Create a copy of the original class record to modify

    while True:
        # Get start time
        print("Start Time")
        new_start = staff_lib.get_time()  # Prompt user for new start time
        if new_start == "0":
            return old_cls  # Return original record if the user cancels

        # Get end time
        print("End Time")
        new_end = staff_lib.get_time()  # Prompt user for new end time
        if new_end == "0":
            return old_cls  # Return original record if the user cancels

        # Ensure end time is after start time
        if time_to_minutes(new_end) <= time_to_minutes(new_start):
            print("End time must be after start time. Please try again.")  # Prevent invalid time selection
            continue

        # Check for scheduling conflicts
        if check_conflict(classes, old_cls["class_id"], old_cls["day"], new_start, new_end, old_cls["location"]):
            print("Conflict detected. Please choose another time.")  # Notify user of conflict
            continue

        # Update start and end times
        new_cls["start_time"] = new_start
        new_cls["end_time"] = new_end

        return new_cls  # Return updated record


def change_location(old_cls, classes):
    """Change the class location while ensuring no conflicts."""

    # Read available locations from file
    loca, header = staff_lib.read_csv_file("./Data/locations.txt")

    print(",".join(header))  # Display location headers
    for location in loca:
        print(",".join(location.values()))  # Display available locations

    new_cls = old_cls.copy()  # Create a copy of the original class record to modify

    while True:
        new_location = input("Enter new location (0 to cancel): ").strip().title()  # Get user input

        if new_location == "0":
            return old_cls  # Return original record if the user cancels

        # Validate if the entered location exists in the dataset
        if staff_lib.search_value("./Data/locations.txt", 0, new_location):
            # Check for scheduling conflicts at the new location
            if check_conflict(classes, old_cls["class_id"], old_cls["day"], old_cls["start_time"], old_cls["end_time"], new_location):
                print("Conflict detected. Please choose another location.")  # Notify user of conflict
                continue

            new_cls["location"] = new_location  # Update location
            return new_cls  # Return updated record

        else:
            print("Invalid location. Please try again.")  # Handle invalid location input
