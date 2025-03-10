import Administrator

def login():
    while True:
        try:
            print("\n" + "=" * 35)
            print("           LOGIN SYSTEM    ")
            print("=" * 35)
            print("1. Login as Administrator")
            print("2. Login as Teacher")
            print("3. Login as Student")
            print("4. Login as Staff")
            print("5. Back")
            print("=" * 35)

            # user input their choice
            choice = int(input("👉 Choose your option by number: "))

            # set user to user's choice for file
            if choice == 1:
                user = "admins"
            elif choice == 2:
                user = "teachers"
            elif choice == 3:
                user = "staffs"
            elif choice == 4:
                user = "students"
            elif choice == 5:
                return  # Exit the Add User menu
            else:
                print("❌ Invalid choice. Please choose again.")
                continue

            print()

            id = str(input("🆔 Enter your ID: "))
            password = str(input("🔑 Enter your password: "))

            file_path = f"../../Data/{user}.txt"

            found = False
            with open(file_path,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if id == data[0] and password == data[2]:
                        found = True

            if not found:
                print("❌ Login Unsuccessfully. Please enter valid ID and password.")
                continue
            else:
                if user == "admins":
                    Administrator.administrator()


        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

while True:
    try:
        print("=" * 46)
        print("| Welcome to the Education Management System |")
        print("=" * 46)
        print("| 1. Login" + " " * 35 + "|")
        print("| 2. Exit" + " " * 36 + "|")
        print("=" * 46)

        user_choice = int(input("👉 Choose your option by number: "))

        if user_choice == 1:
            login()
        elif user_choice ==2:
            print("Exiting the system. Goodbye! Have have nice day ,see you next time !")
            quit()
        else:
            print("❌ Invalid choice. Please choose again.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
