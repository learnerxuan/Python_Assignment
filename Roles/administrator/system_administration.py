def system_administration():
    def add_user():
        """
        Add New User for Admin, Teacher, Staff, and Student
        """
        while True:  # while loop to repeat the process until meet certain condition
            try:
                # Management Menu
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
                    break  # Exit the Add User menu
                else:
                    print("❌ Invalid choice. Please choose again.")
                    continue

                print("\n==================================================")
                print(f"                 ADDING NEW USER                  ")
                print("==================================================")

                # Take input from user and store it into variables
                id = str(input("Enter id: "))
                name = str(input("Enter name: "))
                password = str(input("Enter password: "))
                phone_number = str(input("Enter phone number: "))
                email = str(input("Enter email: "))
                gender_option = int(input("Enter gender (0 - Male, 1 - Female): "))
                # By on gender_option, set gender
                if gender_option == 0:
                    gender = "Male"
                elif gender_option == 1:
                    gender = "Female"
                else:
                    print("Invalid gender choice. Please try again.")
                    continue

                if user == "teachers":
                    faculty_id = str(input("Enter faculty id: "))
                    data = f"{id},{name},{password},{phone_number},{email},{gender},{faculty_id}"
                elif user == "students":
                    data = f"{id},{name},{password},{phone_number},{email},{gender}, - , - "
                else:
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
                print(f" Success! New user has been added.")
                print("==================================================\n")

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

                # Input user choice
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
                    # Exit the update user menu
                    break
                else:
                    print("Invalid choice. Please choose again.")
                    continue

                # Input id of the user who needed to be updated
                id = str(input("Enter id to update: ")).strip()
                found = False
                updated_records = []
                file_path = f"../../Data/{user}.txt"

                with open(file_path, "r") as file:
                    for line in file:
                        all_lines = line.strip().split(",")

                        # Input new data if id is found
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

                            if user == "teachers":
                                new_faculty_id = str(input("Enter faculty id: "))
                                data = f"{id},{new_name},{new_password},{new_phone_number},{new_email},{gender},{new_faculty_id}"
                            elif user == "students":
                                data = f"{id},{new_name},{new_password},{new_phone_number},{new_email},{gender}, - , - "
                            else:
                                data = f"{id},{new_name},{new_password},{new_phone_number},{new_email},{gender}"

                            # Add the updated record
                            updated_records.append(data)
                        else:
                            updated_records.append(line)

                if not found:
                    print(f"User with ID '{id}' not found. Please try again.")
                    continue  # Redisplay the update menu

                # Write updated data back to the file
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
                    print("Invalid choice. Please choose again.")
                    continue

                found = False
                new_record = []
                target_user_id = str(input("Enter user id to be deleted: ")).strip()
                file_path = f"../../Data/{user}.txt"

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
                add_user()
            elif user_choice == 2:
                update_user()
            elif user_choice == 3:
                delete_user()
            elif user_choice == 4:
                return
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

