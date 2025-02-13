from choose import choose
from staff_manage_acc import staff_manage_acc

def staff(staff_id, staff_name):
    print(f"{staff_name}|{staff_id}")
    print("""1. Manage my account
2. Students
3. Timetable
4. Resources
5. Events
6. Communication
7. Log out
0. Exit program""")
    
    choice = choose([0, 1, 2, 3, 4, 5, 6, 7])

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


staff("staff1", "name")