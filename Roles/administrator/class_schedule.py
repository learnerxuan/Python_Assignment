def class_schedule():
    def view_class_schedule():
        """ Display class schedule in a formatted table """
        try:
            # Open the courses.txt file and read the records
            with open("../../Data/schedule.txt", "r") as file:
                # Print the table header
                print("=" * 85)
                print(
                    f"| {'Course ID':<12} | {'Day':<10} | {'Starting Time':<10} | {'Ending Time':<10} | {'Class':<10} | {'Teacher ID':<10} |")
                print("-" * 85)

                # Skip header
                header = file.readline()

                # Print each course record
                for line in file:
                    class_schedule = line.strip().split(",")
                    print(
                        f"| {class_schedule[0]:<12} | {class_schedule[1]:<10} | {class_schedule[2]:<13} | {class_schedule[3]:<11} |{class_schedule[4]:<10}  | {class_schedule[5]:<10} |")

                print("=" * 85)
        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to process the request. Details: {e}")

    def add_class_schedule():
        print("Adding new class...")
        try:
            course_id = str(input("Enter course code: ")).strip()
            # Check whether course code exist
            course_found = False
            teacher_for_course = None
            with open("../../Data/courses.txt", "r") as file:
                for line in file:
                    check_exist = line.strip().split(",")
                    if course_id == check_exist[0]:
                        course_found = True
                        teacher_for_course = check_exist[3]  # The teacher's ID for this course
                        break

            if not course_found:
                print(f"❌ Course code: {course_id} not found")
                return

            day = str(input("Enter day (e.g., Monday): ")).strip()
            start_time = str(input("Enter start time (HH:MM): ")).strip()
            end_time = str(input("Enter end time (HH:MM): ")).strip()
            room = str(input("Enter room number: ")).strip()

            teacher_id = str(input("Enter teacher's id: ")).strip()
            # Check whether instructor exist
            teacher_found = False
            with open("../../Data/teachers.txt", "r") as file:
                for line in file:
                    check_exist = line.strip().split(",")
                    if teacher_id == check_exist[0]:
                        teacher_found = True
                        break

            if not teacher_found:
                print(f"❌ Teacher ID: {teacher_id} not found")
                return

            if teacher_id != teacher_for_course:
                print(f"❌ Error: Teacher ID '{teacher_id}' is not assigned to teach course '{course_id}'.")
                return

            with open("../../Data/schedule.txt", "r") as file:
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

            with open("../../Data/schedule.txt", "a") as file:
                file.write(f"{course_id},{day},{start_time},{end_time},{room},{teacher_id}\n")
            print(f"✅ New schedule for course '{course_id}' added successfully!")

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
            course_id = str(input("Enter Course ID to update: ")).strip()  # Input course code which user wanted update
            found = False
            schedules = []  # Store all rows from the file
            matching_schedules = []  # Store rows matching the course code

            # Check if the course code exist, and store data in respective list.
            with open("../../Data/schedule.txt", "r") as file:
                for line in file:
                    class_schedule = line.strip().split(",")
                    schedules.append(class_schedule)
                    if course_id == class_schedule[0]:
                        found = True
                        matching_schedules.append(class_schedule)
            if not found:
                print(f"❌ Course code '{course_id}' not found.")
                return

            # Display matching schedules in a table
            print("\nCurrent schedule(s) for course code:", course_id)
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
            with open("../../Data/schedule.txt", "w") as file:
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

            with open("../../Data/schedule.txt", "r") as file:
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
                print(
                    f"{'No.':<3}| {'Course Code':<12} | {'Day':<10} | {'Start Time':<10} | {'End Time':<10} | {'Room':<10} | {'Instructor':<10} |")
                print("-" * 85)

                for idx, schedule in enumerate(matching_targeted_class, start=1):
                    print(
                        f"{idx:<3}| {schedule[0]:<12} | {schedule[1]:<10} | {schedule[2]:<10} | {schedule[3]:<10} | {schedule[4]:<10} | {schedule[5]:<10} |")
                print("=" * 85)

                while True:
                    try:
                        row_number = int(input("Enter row number to be deleted: "))
                        if 1 <= row_number <= len(matching_targeted_class):
                            selected_course_code = matching_targeted_class[row_number - 1]
                            break
                        else:
                            print(
                                f"❌ Invalid input. Please enter a number between 1 and {len(matching_targeted_class)}.")
                    except ValueError:
                        print("❌ Invalid input. Please enter a valid number.")
                    except Exception as e:
                        print(f"⚠️ Error: Unable to add new schedule. Details: {e}")

            for schedule in schedules:
                if schedule == selected_course_code:
                    print(f"✅ Class for course code : {targeted_course_code} deleted successfully!")
                else:
                    new_record.append(schedule)

                with open("../../Data/schedule.txt", "w") as file:
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

class_schedule()