def teacher(teacher_id):
    print(f"\n👨‍🏫 Welcome, Teacher {teacher_id}!\n")

    while True:
        print("\n===== Teacher Course Management System =====")
        print("1) Manage Classes")
        print("2) Student Enrollment")
        print("3) Grade Assignment and Assessment")
        print("4) Track Attendance")
        print("5) Generate Report")
        print("6) Exit")
        print("===========================================\n")

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            from Manage_class import manage_classes  # Ensure correct filename
            manage_classes(teacher_id)
        elif choice == "2":
            from student_enrollment import student_enrollment
            student_enrollment()
        elif choice == "3":
            from Grade_Assignment import grade_assignment  # Ensure correct filename
            grade_assignment(teacher_id)
        elif choice == "4":
            from Track_Attendance import track_attendance  # Ensure correct filename
            track_attendance(teacher_id)
        elif choice == "5":
            from Generate_Report import generate_report  # Ensure correct filename
            generate_report(teacher_id)
        elif choice == "6":
            print("\n🎓 Thank You for using the Teacher Course Management System. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 6.\n")


