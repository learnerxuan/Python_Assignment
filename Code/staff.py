def staff(staff_id, staff_name):
    print(f"{staff_name}|{staff_id}")
    print("""1. Manage my account
    2. Students
    3. Timetable
    4. Resources
    5. Events
    6. Communication
    7. Log out
    8. Exit program""")
    staff_choice = [1, 2, 3, 4, 5, 6, 7, 8]
    choice = choose(staff_choice)

    if choice == 1:
        staff_manage_acc()
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
    elif choice == 8:
        exit("Program Exited")


def choose(choice):
    while True:
        try:
            num = int(input(f"Enter number ({choice[0]}-{choice[-1]}): "))
            if num in choice:
                return num
            else:
                print(f"Please enter a number between {choice[0]} and {choice[-1]}.")
        except ValueError:
            print(f"Invalid input. Please enter a number between {choice[0]} and {choice[-1]}.")


def staff_manage_acc():
    pass


staff("id", "name")