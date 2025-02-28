import color
import staff_lib
from staff_manage_acc import staff_manage_acc
from student_rec import student_rec
from resources import resources
from events import events
from communication import communication


def staff(staff_id, staff_name):
    """Displays the staff menu and processes user navigation."""
    while True:
        # Display the staff menu
        print(staff_id, staff_name)
        print(f"{"=" * 20}{color.BOLD} STAFF MENU {color.RESET}{"=" * 20}")
        print(f"""{" " * 17}1. Manage my account
{" " * 17}2. Students
{" " * 17}3. Timetable
{" " * 17}4. Resources
{" " * 17}5. Events
{" " * 17}6. Communication
{" " * 17}7. Log out
{" " * 17}0. Exit program""")
        print(f"=" * 52)

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6, 7])

        # Navigate based on user choice
        if choice == 1:
            staff_manage_acc(staff_id, staff_name)
        elif choice == 2:
            student_rec()
        elif choice == 3:
            manage_timetable() 
        elif choice == 4:
            resources()
        elif choice == 5:
            events()
        elif choice == 6:
            communication()
        elif choice == 7:
            main()
        elif choice == 0:
            exit("Program Exited")


staff("S001", "name")