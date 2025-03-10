import libraries


def system_administration():
    """
    Manage teachers, staffs, student and admins' accounts and credentials.
    """
    def view_user():
        """
        Display all users in a formatted table.
        """
        try:
            while True:
                print("\n" + "=" * 50)
                print("               VIEW USERS MENU               ")
                print("=" * 50)
                print("1. View Admin Users")
                print("2. View Teacher Users")
                print("3. View Staff Users")
                print("4. View Student Users")
                print("5. View Parent Info")
                print("6. Back")
                print("=" * 50)

                choice = int(input("👉 Choose your option by number: "))

                # set user to user's choice for file purpose
                if choice == 1:
                    user = "admins"
                elif choice == 2:
                    user = "teachers"
                elif choice == 3:
                    user = "staffs"
                elif choice == 4:
                    user = "students"
                elif choice == 5:
                    user = "parents"  # Exit the Add User menu
                elif choice == 6:
                    break
                else:
                    print("❌ Invalid choice. Please choose again.")
                    continue

                # Print out Parents data in table form
                if choice == 5:
                    with open(f"../../Data/{user}.txt", "r") as file:
                        # Skip header
                        file.readline()

                        # Print the table header
                        print("=" * 129)
                        print(f"| {'ID':<15} | {'Student ID':<15} | {'Name':<20} | {'Phone Number':<20} | {'Email':<30} | {'Gender':<10} |")
                        print("-" * 129)

                        # Print each record
                        for line in file:
                            record = line.strip().split(",")
                            if len(record) == 6:
                                print(f"| {record[0]:<15} | {record[1]:<15} | {record[2]:<20} | {record[3]:<20} | {record[4]:<30} | {record[5]:<10} |")

                        print("=" * 129)

                # Print out Students data in table form
                elif choice == 4:
                    """ View students personal details from students.txt"""

                    # Store all data from students.txt to students dictionary
                    print("\n" + "=" * 150)
                    print(
                        f"| {'ID':<10} | {'Name':<20} | {'Password':<15} | {'Phone Number':<15} | {'Email':<27} | {'Gender':<10} | {'Enrollment Status':<18} | {'Parent ID':<10} |")
                    print("-" * 150)

                    with open("../../Data/students.txt", "r") as file:
                        # Skip header
                        file.readline()

                        for line in file:
                            data = line.strip().split(",")
                            print(
                                f"| {data[0]:<10} | {data[1]:<20} | {data[2]:<15} | {data[3]:<15} | {data[4]:<27} | {data[5]:<10} | {data[6]:<18} | {data[7]:<10} |")

                    print("=" * 150)

                # Print out admins,staffs and teachers data in table form
                elif choice == 1 or choice == 2 or choice == 3:
                    with open(f"../../Data/{user}.txt", "r") as file:
                        # Skip header
                        file.readline()

                        # Print the table header
                        print("=" * 116)
                        print(f"| {'ID':<12} | {'Name':<15} | {'Password':<15} | {'Phone Number':<15} | {'Email':<30} | {'Gender':<10} |")
                        print("-" * 116)

                        # Print each record
                        for line in file:
                            record = line.strip().split(",")
                            if len(record) == 6:
                                print(f"| {record[0]:<12} | {record[1]:<15} | {record[2]:<15} | {record[3]:<15} | {record[4]:<30} | {record[5]:<10} |")

                        print("=" * 116)
                else:
                    print("❌ Invalid choice. Please choose again.")
                    continue

        except FileNotFoundError as e:
            print(f"❌ Error: {e.filename} file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"⚠️ Error: Unable to read student records. Details: {e}")

    def add_user():
        """
        Add new user for admin, teacher, staff, and student
        When inputting student's details, need to input their parent's details too
        """
        while True:  # while loop to repeat the process until meet certain condition
            try:
                # User Management Menu
                print("\n==================================================")
                print("                  USER MANAGEMENT                 ")
                print("==================================================")
                print("1. Add User for Admin")
                print("2. Add User for Teacher")
                print("3. Add User for Staff")
                print("4. Add User for Student")
                print("5. Back")
                print("==================================================")

                # user input their choice
                choice = int(input("👉 Choose your option by number: "))

                # set user to user's choice for file and prefix purpose
                if choice == 1:
                    user = "admins"
                elif choice == 2:
                    user = "teachers"
                elif choice == 3:
                    user = "staffs"
                elif choice == 4:
                    user = "students"
                elif choice == 5:
                    break  # Exit the Add User menu
                else:
                    print("❌ Invalid choice. Please choose again.")
                    continue

                print("\n==================================================")
                print(f"                 ADDING NEW USER                  ")
                print("==================================================")

                name = input("Enter name (or type 'exit' to return): ").strip()
                if name.lower() == "exit":
                    continue # Return back to the menu

                password = input("Enter password: ").strip()
                if password.lower() == "exit":
                    continue

                phone_number = input("Enter phone number: ").strip()
                if phone_number.lower() == "exit":
                    continue

                email = input("Enter email: ").strip()
                if email.lower() == "exit":
                    continue

                while True:
                    gender_option = input("Enter gender (0 - Male, 1 - Female, or 'exit' to return): ").strip().lower()
                    if gender_option == "exit":
                        break
                    elif gender_option == "0":
                        gender = "Male"
                        break
                    elif gender_option == "1":
                        gender = "Female"
                        break
                    else:
                        print("❌ Invalid gender choice. Please try again.")

                if gender_option == "exit":
                    continue  # Return back to User Management Menu

                if user == "teachers":
                    id = libraries.generate_new_id("../../Data/teachers.txt", "T")
                    data = f"{id},{name},{password},{phone_number},{email},{gender}"
                elif user == "students":
                    id = libraries.generate_new_id("../../Data/students.txt", "S")

                    # Add student's parent details
                    print("Fill in parents details: ")
                    exit = False
                    while True:
                        name = input("Enter parent name (or type 'exit' to return): ").strip()
                        if name.lower() == "exit":
                            exit = True
                            break # return back to the menu

                        phone_number = input("Enter phone number: ").strip()
                        if phone_number.lower() == "exit":
                            exit = True
                            break

                        email = input("Enter email: ").strip()
                        if email.lower() == "exit":
                            exit = True
                            break


                        while True:
                            gender_option = input(
                                "Enter gender (0 - Male, 1 - Female, or 'exit' to return): ").strip().lower()
                            if gender_option == "exit":
                                break
                            elif gender_option == "0":
                                gender = "Male"
                                break
                            elif gender_option == "1":
                                gender = "Female"
                                break
                            else:
                                print("❌ Invalid gender choice. Please try again.")

                        if gender_option == "exit":
                            exit = True
                            break  # Return back to User Management Menu

                        parent_id = libraries.generate_new_id("../../Data/parents.txt", "P")
                        data = f"{id},{name},{password},{phone_number},{email},{gender},None,{parent_id}"
                        parent_data = f"{parent_id},{id},{name},{phone_number},{email},{gender}"
                        with open("../../Data/parents.txt", "a+") as file:
                            file.seek(0)  # Move the cursor to the beginning of the file
                            content = file.read()
                            if content and not content.endswith("\n"):  # Ensure no extra blank lines
                                file.write("\n")
                            # Write all the data into file
                            file.write(parent_data)

                            break

                    if exit == True:
                        continue
                elif user == "staffs":
                    id = libraries.generate_new_id("../../Data/staffs.txt", "STF")
                    data = f"{id},{name},{password},{phone_number},{email},{gender}"
                else:
                    id = libraries.generate_new_id("../../Data/admins.txt", "A")
                    data = f"{id},{name},{password},{phone_number},{email},{gender}"

                # Save all variables into the respective file
                file_path = f"../../Data/{user}.txt"
                with open(file_path, "a+") as file:
                    file.seek(0)  # Move the cursor to the beginning of the file
                    content = file.read()
                    if content and not content.endswith("\n"):  # Ensure no extra blank lines
                        file.write("\n")
                    # Write all the data into file
                    file.write(data)

                print("--------------------------------------------------")
                print(f"✅ Success! New user with ID '{id}' has been added.")
                print("==================================================\n")

            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")

    def update_user():
        """
        Update user by inputting user id
        """
        while True:  # Loop to redisplay the update menu
            try:
                print("\n==================================================")
                print("                  USER MANAGEMENT                 ")
                print("==================================================")
                print("1. Update Admin User")
                print("2. Update Teacher User")
                print("3. Update Staff User")
                print("4. Back")
                print("==================================================")

                # Input user choice
                choice = int(input("👉 Choose your option by number: "))

                if choice == 1:
                    user = "admins"
                elif choice == 2:
                    user = "teachers"
                elif choice == 3:
                    user = "staffs"
                elif choice == 4:
                    # Exit the update user menu
                    break
                else:
                    print("❌ Invalid choice. Please choose again.")
                    continue # Restart the loop if invalid choice

                file_path = f"../../Data/{user}.txt"

                # Input ID of the user to update
                while True:
                    id = input("Enter user ID to update (or type 'exit' to return): ").strip()
                    if id.lower() == "exit":
                        break  # Return back to User Management Menu

                    found = False
                    updated_records = [] # Store updated data

                    exit = False
                    with open(file_path, "r") as file:
                        for line in file:
                            all_lines = line.strip().split(",")

                            # If ID is found, allow updates
                            if all_lines[0] == id:
                                found = True
                                print(f"Updating record for user ID: {id}")
                                new_name = input("Enter new name (or press Enter to keep current name): ").strip() or \
                                           all_lines[1]
                                if new_name.lower() == "exit":
                                    exit = True
                                    break


                                new_password = input(
                                    "Enter new password (or press Enter to keep current password): ").strip() or \
                                               all_lines[2]
                                if new_password.lower() == "exit":
                                    exit = True
                                    break


                                new_phone_number = input(
                                    "Enter new phone number (or press Enter to keep current phone number): ").strip() or \
                                                   all_lines[3]
                                if new_phone_number.lower() == "exit":
                                    exit = True
                                    break

                                new_email = input("Enter new email (or press Enter to keep current email): ").strip() or \
                                            all_lines[4]
                                if new_email.lower() == "exit":
                                    exit = True
                                    break

                                # Update gender
                                while True:
                                    gender_input = input(
                                        "Enter gender (0 - Male, 1 - Female) (or press Enter to keep current gender): ").strip().lower()
                                    if gender_input == "exit":
                                        exit = True
                                        break
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

                                data = f"{id},{new_name},{new_password},{new_phone_number},{new_email},{gender}"

                                updated_records.append(data + "\n")
                            else:
                                updated_records.append(line)
                    if exit:
                        break

                    if not found:
                        print(f"❌ User with ID '{id}' not found. Please try again.")
                        continue  # Redisplay the update menu

                    # Write updated data back to the file
                    with open(file_path, "w") as file:
                        file.writelines(updated_records)

                    print(f"✅ User ID: {id} record updated successfully!")
                    break

            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")

    def delete_user():
        while True:
            try:
                # Display delete table
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
                    user = "admins"
                elif choice == 2:
                    user = "teachers"
                elif choice == 3:
                    user = "staffs"
                elif choice == 4:
                    user = "students"
                elif choice == 5:
                    break
                else:
                    print("❌ Invalid choice. Please choose again.")
                    continue

                file_path = f"../../Data/{user}.txt"

                while True:
                    target_user_id = input("Enter user ID to be deleted (or type 'exit' to return): ").strip()
                    if target_user_id.lower() == "exit":
                        break  # Return to the menu

                    parent_id_to_delete = None
                    found = False
                    new_records = []

                    with open(file_path, "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            if data[0] == target_user_id:
                                found = True
                                # If deleting a student, store their parent ID
                                if user == "students" and len(data) > 7:
                                    parent_id_to_delete = data[7] # Store parent ID

                            else:
                                new_records.append(line)

                    if not found:
                        print(f"❌ ID '{target_user_id}' not found. Please try again.")
                        continue

                    # Write updated records back to the user file
                    with open(file_path, "w") as file:
                        file.writelines(new_records)
                    print(f"✅ Record of ID '{target_user_id}' has been deleted.")

                    # Delete parent ID of the student from parents.txt
                    if user == "students" and parent_id_to_delete:
                        parent_file_path = "../../Data/parents.txt"
                        parent_records = []
                        parent_found = False

                        with open(parent_file_path, "r") as parent_file:
                            for line in parent_file:
                                parent_data = line.strip().split(",")
                                if parent_data[0] == parent_id_to_delete:
                                    parent_found = True
                                else:
                                    parent_records.append(line)

                        if parent_found:
                            with open(parent_file_path, "w") as parent_file:
                                parent_file.writelines(parent_records)
                            print(f"✅ Parent record with ID '{parent_id_to_delete}' also deleted.")
                        else:
                            print(f"⚠️ Parent record with ID '{parent_id_to_delete}' not found.")

                    break

            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred: {e}")

    # System Administration Menu
    while True:
        print("\n" + "=" * 50)
        print("                SYSTEM ADMINISTRATION               ")
        print("=" * 50)
        print("1. View User")
        print("2. Add User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Back")
        print("=" * 50)

        try:
            # user input their choice
            user_choice = int(input("👉 Choose your option by number: "))
            print("=" * 50)

            if user_choice == 1:
                view_user()
            elif user_choice == 2:
                add_user()
            elif user_choice == 3:
                update_user()
            elif user_choice == 4:
                delete_user()
            elif user_choice == 5:
                return
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

system_administration()

