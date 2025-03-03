import color
import staff_lib
from staff_manage_acc import staff_manage_acc
from student_rec import student_rec
from manage_timetable import manage_timetable
from resources import resources
from events import events
from communication import communication


def staff(staff_id, staff_name):
    """Displays the staff menu and processes user navigation."""
    while True:
        # Display the staff menu
        print(f"\n{color.BOLD}{color.BLUE}STAFF ID:{color.RESET} {staff_id}   {color.BOLD}{color.BLUE}NAME:{color.RESET} {staff_name}\n")
        print(f"{'=' * 20}{color.BOLD}{color.BLUE} STAFF MENU {color.RESET}{'=' * 20}")
        print(f"""{" " * 15}{color.YELLOW}1.{color.RESET}  Manage My Account
{" " * 15}{color.YELLOW}2.{color.RESET}  Students
{" " * 15}{color.YELLOW}3.{color.RESET}  Timetable
{" " * 15}{color.YELLOW}4.{color.RESET}  Resources
{" " * 15}{color.YELLOW}5.{color.RESET}  Events
{" " * 15}{color.YELLOW}6.{color.RESET}  Communication
{" " * 15}{color.YELLOW}7.{color.RESET}  Log Out
{" " * 15}{color.YELLOW}0.{color.RESET}  Exit Program""")
        print(f"{'=' * 52}")

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


staff("STF001", "Alice Johnson")