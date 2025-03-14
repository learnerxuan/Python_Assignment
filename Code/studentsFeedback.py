def next_feedbackid(): # generate the next feedback_id
    try:
        with open("feedbacks.txt","r") as f:
            lines = f.readlines()
            if lines: 
                last_line = lines[-1].strip()
                last_id = last_line.split(",")[0]
                if last_id.startswith("FB") and last_id[2:].isdigit():
                    next_id = int(last_id[2:]) + 1
                    return f"FB{next_id:03d}"
                else:
                    return "FB001"
            else:
                return "FB001"
    except FileNotFoundError:
        return "FB001"

def feedback_academic(student_id):
    feedback_id = next_feedbackid()    
    print("\n======= Overall Academic Feedback =======")
    target_id = "General"
    print(f"Target: {target_id}")
    feedback_ac = input("\nEnter your overall feedback on your academic experience at the University : \n")
    response = "None"
    with open ("feedbacks.txt","a") as f:
        f.write(f"{feedback_id},{student_id},{target_id},{feedback_ac},{response}\n")
    return

def feedback_instructors(student_id):
    print("\n========== Instructor Feedback ==========")
    target_id = input("Enter the instructor ID : ")
    feedback_in = input("Enter your feedback on your instructors at the University : \n")
    feedback_id = next_feedbackid()
    response = "None"
    with open ("feedbacks.txt","a") as f:
        f.write(f"{feedback_id},{student_id},{target_id},{feedback_in},{response}\n")
    return

def feedback_course(student_id):
    print("\n========== Course Feedback ==========")
    target_id = input("Enter the course ID : ")
    feedback_co = input("\nEnter your feedback on your course at the University : \n")
    feedback_id = next_feedbackid()
    response = "None"
    with open ("feedbacks.txt","a") as f:
        f.write(f"{feedback_id},{student_id},{target_id},{feedback_co},{response}\n")
    return

def studentFeedback(student_id):
    with open ("students.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == student_id:
                student_details = data
                
    with open ("feedbacks.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == student_id:
                feedback_details = data
                
    print("\n========== Student Feedback ==========")
    print(f"Student ID: {student_id}\nStudent Name: {student_details[1]}")
    print("======================================")
    print("|  1 | Course Feedback               |")
    print("|  2 | Instructor Feedback           |")
    print("|  3 | Overall Academic Experience   |")
    print("|  0 | Previous Page                 |")
    print("======================================")
    
    while True:
        choice = input("Please enter an option (0~3): ")
        if choice == "1":
            feedback_course(student_id)
        elif choice == "2":
            feedback_instructors(student_id)
        elif choice == "3":
            feedback_academic(student_id)
        elif choice == "0":
            import students
            students.students(student_id)
            return
        else:
            print("\nPlease try again and enter a valid choice.\n")