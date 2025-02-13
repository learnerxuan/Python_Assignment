import staff_lib


def student_rec():
    """Display student record menu and processes user choices."""
    while True:
        print("""
1. Students' Course Registration
2. Transfer Course
3. Course Withdrawal
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3])

        if choice == 1:
            stu_course_reg()
        elif choice == 2:
            stu_trans_course()
        elif choice == 3:
            stu_course_withdraw()
        elif choice == 0:
            # Return back to staff menu
            return
        

def stu_course_reg():
    pass