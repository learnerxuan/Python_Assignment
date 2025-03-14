def students(student_id): # VERY MAIN
    with open("../Data/students.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == student_id:
                student_details = data          

    print("\n========== Student Menu ==========")
    print(f"Student ID: {student_id} \nStudent Name: {student_details[1]}")
    print("==================================")
    print("|      1 | Manage Account        |")
    print("|      2 | Courses               |")
    print("|      3 | Course Material       |")
    print("|      4 | Feedback              |")
    print("|      0 | Exit                  |")
    print("==================================")
    while True:
        choice = input("Please enter an option (0~4) : ")
        if choice == "1":
            import studentsManage
            studentsManage.studentsManage(student_id)
        elif choice == "2":
            import studentsCourse
            studentsCourse.studentsCourse(student_id)
        elif choice == "3":
            import studentsCourseMAT
            studentsCourseMAT.studentsCourseMAT(student_id)
        elif choice == "4":
            import studentsFeedback
            studentsFeedback.studentFeedback(student_id)
        elif choice == "0":
            return
        else:
            print("\nPlease try again and enter a valid choice.\n")
