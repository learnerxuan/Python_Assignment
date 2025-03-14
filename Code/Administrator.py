import system_administration
import student_management
import class_schedule
import course_management
import report_generation
import libraries

def administrator():
    """
    Administrator menu that display all functions available as an administrator.
    """

    while True: # while loop to repeat the process until meet certain condition
        try:
            # Administrator menu
            print("\n" + "=" * 73)
            print(" " * 22 + "Administrator Menu")
            print("=" * 73)
            print(f"| {'No.':<3} | {'Function':<26} | {'Description':<34} |")
            print("-" * 73)
            print(f"| 1   | System Administration      | View, Add, Update, Delete User     |")
            print(f"| 2   | Student Management         | View, Update Student Record        |")
            print(f"| 3   | Course Management          | View, Add, Update, Delete Course   |")
            print(f"| 4   | Class Schedule             | View, Add, Update Schedule         |")
            print(f"| 5   | Report Generation          | Performance, Attendance, Finance   |")
            print(f"| 6   | Logout                     | Return to Login Screen             |")
            print(f"| 7   | Exit                       | Exit the System                    |")
            print("=" * 73)

            # user input their choice
            admin_choice = int(input("👉 Choose your option by number: "))
            print("=" * 73)

            if admin_choice == 1:
                system_administration.system_administration()
            elif admin_choice == 2:
                student_management.student_management()
            elif admin_choice == 3:
                course_management.course_management()
            elif admin_choice == 4:
                class_schedule.class_schedule()
            elif admin_choice == 5:
                report_generation.report_generation()
            elif admin_choice == 6:
                print("Logging out...")
                return
            elif admin_choice == 7:
                print("Exiting the system. Goodbye! Have have nice day ,see you next time !")
                quit()
            else:
                print("❌ Invalid choice. Please choose again.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

