import libraries
def class_schedule():
    def view_class_schedule():
        """
        Display class schedule in a formatted table
        """
        try:
            # Open the courses.txt file and read the records
            with open("./../Data/classes.txt", "r") as file:
                # Print the table header
                print("=" * 108)
                print(f"| {'Class ID':<12} | {'Course ID':<10} | {'Teacher ID':<13} | {'Day':<11} | {'Starting Time':<15} | {'Ending Time':<15} | {'Location':<10} |")
                print("-" * 108)

                # Skip header
                file.readline()

                # Print class timetable table
                for line in file:
                    class_schedule = line.strip().split(",")
                    if len(class_schedule) < 10:
                        continue
                    print(f"| {class_schedule[0]:<12} | {class_schedule[1]:<10} | {class_schedule[2]:<13} | {class_schedule[3]:<11} | {class_schedule[4]:<15} | {class_schedule[5]:<15} | {class_schedule[6]:<10} |")

                print("=" * 108)
        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to process the request. Details: {e}")

    def add_class_schedule():
        print("Adding new class...")

        try:
            while True:
                course_id = input("Enter course ID (or type 'exit' to cancel): ").strip()
                if course_id.lower() == "exit":
                    return # Return back to the menu

                course_exists = False
                with open("../../Data/courses.txt", "r") as file:
                    file.readline()  # Skip header
                    for line in file:
                        check_exist = line.strip().split(",")
                        if len(check_exist) > 0 and check_exist[0] == course_id:
                            course_exists = True
                            break

                if not course_exists:
                    print(f"❌ Error: Course ID '{course_id}' not found. Please enter an existing course ID.")
                else:
                    break

            # Validate day input
            valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
            while True:
                day = input("Enter day (e.g., Monday): ").strip().lower()
                if day == "exit":
                    return
                if day not in valid_days:
                    print("❌ Invalid day. Please enter a valid day (Monday - Friday).")
                else:
                    break

            # Time validation function
            def is_valid_time(time_str):
                if len(time_str) != 5 or time_str[2] != ":":
                    return False
                hh, mm = time_str[:2], time_str[3:]
                return hh.isdigit() and mm.isdigit() and 0 <= int(hh) <= 23 and 0 <= int(mm) <= 59

            # Convert HH:MM to total minutes
            def time_to_minutes(time_str):
                hh, mm = time_str.split(":")
                return int(hh) * 60 + int(mm)

            # Input start time
            while True:
                start_time = input("Enter start time (HH:MM): ").strip()
                if start_time.lower() == "exit":
                    return
                if is_valid_time(start_time):
                    break
                print("❌ Invalid time format! Please enter time in HH:MM format.")

            # Input end time
            while True:
                end_time = input("Enter end time (HH:MM): ").strip()
                if end_time.lower() == "exit":
                    return
                if is_valid_time(end_time) and time_to_minutes(end_time) > time_to_minutes(start_time):
                    break
                print("❌ Invalid time! End time must be later than start time and in HH:MM format.")

            # Display available locations
            print("=" * 42)
            print(f"| {'Location':<25} | {'Capacity':<10} |")
            print("-" * 42)
            available_locations = [] # Store available locations
            with open("../../Data/locations.txt", "r") as file:
                file.readline()  # Skip header
                for line in file:
                    location = line.strip().split(",")
                    if len(location) >= 2:
                        available_locations.append(location[0])
                        print(f"| {location[0]:<25} | {location[1]:<10} |")
            print("=" * 42)

            # Input location
            while True:
                location = input("Enter location: ").strip()
                if location.lower() == "exit":
                    return
                if location in available_locations:
                    break
                print(f"❌ Location '{location}' not found. Please enter an existing location.")

            # Check for scheduling conflicts
            new_start_minutes = time_to_minutes(start_time)
            new_end_minutes = time_to_minutes(end_time)

            with open("../../Data/classes.txt", "r") as file:
                file.readline()  # Skip header
                for line in file:
                    check_exist = line.strip().split(",")
                    if len(check_exist) >= 7:
                        # Extract scheduled values
                        scheduled_day = check_exist[3].strip().lower()
                        scheduled_start = check_exist[4].strip()
                        scheduled_end = check_exist[5].strip()
                        scheduled_room = check_exist[6].strip()

                        scheduled_start_minutes = time_to_minutes(scheduled_start)
                        scheduled_end_minutes = time_to_minutes(scheduled_end)

                        # Room conflict
                        if scheduled_day == day and scheduled_room.lower() == location.lower():
                            if new_end_minutes > scheduled_start_minutes and new_start_minutes < scheduled_end_minutes:
                                print("❌ Conflict detected: The room is already reserved for that time.")
                                return

            # Write new class schedule
            class_id = libraries.generate_new_id("../../Data/classes.txt", "CLS")
            with open("../../Data/classes.txt", "a") as file:
                # Use "None" for teacher_id, and "" for lesson_plan, notes, announcement
                file.write(f"{class_id},{course_id},None,{day.capitalize()},{start_time},{end_time},{location},None,None,None\n")

            print(f"✅ New class ID '{class_id}' for course '{course_id}' added successfully!")

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to add new schedule. Details: {e}")

    def update_class_schedule():
        print("Updating class schedule...")

        try:
            # Input class ID to update
            while True:
                class_id = input("Enter class ID to update (or type 'exit' to cancel): ").strip()
                if class_id.lower() == "exit":
                    return

                found = False
                updated_records = []

                # Read current class records
                with open("../../Data/classes.txt", "r") as file:
                    header = file.readline()  # Save header
                    for line in file:
                        check_exist = line.strip().split(",")
                        if len(check_exist) >= 7 and check_exist[0] == class_id:
                            found = True

                            print(f"Updating schedule for Class ID: {class_id}")

                            # Get existing details
                            course_id, teacher_id, day, start_time, end_time, location, lesson_plan, notes, announcement = check_exist[1], check_exist[2], check_exist[3], check_exist[4], check_exist[5], check_exist[6],check_exist[7], check_exist[8], check_exist[9]

                            # Validate day input
                            valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

                            while True:
                                new_day = input(
                                    f"Enter new day (or press Enter to keep '{day}'): ").strip().capitalize()

                                if new_day.lower() == "exit":
                                    return  # Return back to the menu

                                if new_day == "":
                                    new_day = day  # Keep existing day if Enter is pressed

                                if new_day not in valid_days:
                                    print("❌ Invalid day. Please enter a valid day (Monday - Friday).")
                                else:
                                    break  # Valid input, exit the loop

                            # Time validation function
                            def is_valid_time(time_str):
                                if len(time_str) != 5 or time_str[2] != ":":
                                    return False
                                hh, mm = time_str[:2], time_str[3:]
                                return hh.isdigit() and mm.isdigit() and 0 <= int(hh) <= 23 and 0 <= int(mm) <= 59

                            # Convert HH:MM to total minutes
                            def time_to_minutes(time_str):
                                hh, mm = time_str.split(":")
                                return int(hh) * 60 + int(mm)

                            # Input new start time
                            while True:
                                new_start_time = input(
                                    f"Enter new start time (or press Enter to keep '{start_time}'): ").strip() or start_time
                                if new_start_time.lower() == "exit":
                                    return
                                if is_valid_time(new_start_time):
                                    break
                                print("❌ Invalid time format! Please enter time in HH:MM format.")

                            # Input new end time
                            while True:
                                new_end_time = input(
                                    f"Enter new end time (or press Enter to keep '{end_time}'): ").strip() or end_time
                                if new_end_time.lower() == "exit":
                                    return
                                if is_valid_time(new_end_time) and time_to_minutes(new_end_time) > time_to_minutes(
                                        new_start_time):
                                    break
                                print("❌ Invalid time! End time must be later than start time and in HH:MM format.")

                            # Display available locations
                            print("=" * 42)
                            print(f"| {'Location':<25} | {'Capacity':<10} |")
                            print("-" * 42)
                            available_locations = []
                            with open("../../Data/locations.txt", "r") as file:
                                file.readline()  # Skip header
                                for loc in file:
                                    loc_data = loc.strip().split(",")
                                    if len(loc_data) >= 2:
                                        available_locations.append(loc_data[0])
                                        print(f"| {loc_data[0]:<25} | {loc_data[1]:<10} |")
                            print("=" * 42)

                            # Input new location
                            while True:
                                new_location = input(
                                    f"Enter new location (or press Enter to keep '{location}'): ").strip() or location
                                if new_location.lower() == "exit":
                                    return
                                if new_location in available_locations:
                                    break
                                print(f"❌ Location '{new_location}' not found. Please enter an existing location.")

                            # Check for scheduling conflicts
                            new_start_minutes = time_to_minutes(new_start_time)
                            new_end_minutes = time_to_minutes(new_end_time)

                            with open("../../Data/classes.txt", "r") as file:
                                file.readline()  # Skip header
                                for other_class in file:
                                    check_exist = other_class.strip().split(",")
                                    if len(check_exist) >= 7 and check_exist[0] != class_id:
                                        scheduled_day = check_exist[3].strip().lower()
                                        scheduled_start = check_exist[4].strip()
                                        scheduled_end = check_exist[5].strip()
                                        scheduled_room = check_exist[6].strip()

                                        scheduled_start_minutes = time_to_minutes(scheduled_start)
                                        scheduled_end_minutes = time_to_minutes(scheduled_end)

                                        # Room conflict
                                        if scheduled_day == new_day and scheduled_room.lower() == new_location.lower():
                                            if new_end_minutes > scheduled_start_minutes and new_start_minutes < scheduled_end_minutes:
                                                print("❌ Conflict detected: The room is already reserved for that time.")
                                                return

                            # Update the record
                            updated_records.append(f"{class_id},{course_id},{teacher_id},{new_day.capitalize()},{new_start_time},{new_end_time},{new_location},{lesson_plan},{notes},{announcement}\n")
                        else:
                            updated_records.append(line)

                if not found:
                    print(f"❌ Error: Class ID '{class_id}' not found.")
                    return

                # Write updated data back to the file
                with open("../../Data/classes.txt", "w") as file:
                    file.write(header)  # Write the header back
                    file.writelines(updated_records)

                print(f"✅ Class ID '{class_id}' updated successfully!")
                return

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to update schedule. Details: {e}")

    def delete_class_schedule():
        """ Delete a class schedule for a given Class ID """
        try:
            print("Deleting class...")

            while True:
                class_found = False # Used to check exist
                new_record = []

                delete_class_id = str(input("Enter class ID of the class to be deleted (or type 'exit' to cancel):")).strip()

                if delete_class_id.lower() == "exit":
                    return

                with open("../../Data/classes.txt","r") as file:
                    for line in file:
                        classes = line.strip().split(",")
                        if delete_class_id == classes[0]:
                            class_found = True
                            print(f"✅ Class ID '{delete_class_id}' is deleted.")
                        else:
                            new_record.append(line)

                if not class_found:
                    print(f"❌ Class ID '{delete_class_id}' not found")
                else:
                    with open("../../Data/classes.txt", "w") as file:
                        file.writelines(new_record)
                    return  # Return back to the menu



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

# class_schedule()
