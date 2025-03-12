
def teacher():
    teacher_id=input("Enter Your teacher_id:").strip()

    if not teacher_id:
        print("teacher_id not exist. Please try again!")
        return

    print(f"Welcome,Teacher {teacher_id}")

    while True:
       print("Teacher Course Management System")
       print("1)Manage Courses")
       print("2)Student Enrollment")
       print("3)Grade Assignment and Assessment")
       print("4)Track Attendance")
       print("5)Generate Report")
       print("6)Exit")


       choice = input("Enter Your Choice:").strip()


       if choice == "1":
           from main.Manage_course import manage_courses
           manage_courses(teacher_id)
       elif choice == "2":
           from main.student_enrollment import student_enrollment
           student_enrollment()
       elif choice == "3":
           from main.Grade_Assignment import grade_assignment
           grade_assignment(teacher_id)
       elif choice == "4":
           from main.Track_Attendance import track_attendance
           track_attendance(teacher_id)
       elif choice == "5":
           from main.Generate_Report import generate_report
           generate_report(teacher_id)
       elif choice == "6":
           print("Thank You for using Teacher Course Management System")
           break
       else:
           print("Invalid Choice")
teacher()

