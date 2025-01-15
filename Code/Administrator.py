def administrator():
    def system_administration():
        def add_user():
            new_username = str(input("Enter new username: "))
            new_password = int(input("Enter new password: "))
            user_role = ""
            while True:
                print("Enter role for this user\n1. Administrator\n2. Teacher\n3. Student\n4. Staff")
                role_choice = int(input("Choose your role by number: "))
                if role_choice == 1:
                    user_role = "Administrator"
                    break
                elif role_choice == 2:
                    user_role = "Teacher"
                    break
                elif role_choice == 3:
                    user_role = "Teacher"
                    break
                elif role_choice == 4:
                    user_role = "Staff"
                    break
                else:
                    print("Invalid choice. Please choose again")
            print(new_username,new_password,user_role)

        def update_user():
            ...

        def delete_user():
            ...

        while True:
            print("System Administration:\n1. Add User\n2. Update User\n3. Delete User")
            user_choice = int(input("Choose your option by number: "))
            if user_choice == 1:
                add_user()
            elif user_choice == 2:
                update_user()
            elif user_choice == 3:
                delete_user()
            else:
                print("Invalid choice.Please choose again")



    def student_management():
        print("hello world")

    def course_management():
        print("hello world")

    def class_schedule():
        print("hello world")

    def report_generation():
        print("hello world")

    def logout():
        print("Logging Out....")

    def quit():
        print("Exiting.... Bye")


    while True:
        print("Administrator Menu: "
              "\n1. System Administration "
              "\n2. Student Management"
              "\n3. Course Management"
              "\n4. Class Schedule"
              "\n5. Report Generation"
              "\n6. Logout"
              "\n7. Exit")
        admin_choice = int(input("Choose your option by number: "))
        if admin_choice == 1:
            system_administration()

        elif admin_choice == 2:
            student_management()

        elif admin_choice == 3:
            course_management()

        elif admin_choice == 4:
            class_schedule()

        elif admin_choice == 5:
            report_generation()

        elif admin_choice == 6:
            logout()

        elif admin_choice == 7:
            quit()
            break

        else:
            print("Invalid choice. Please choose again")

administrator()






