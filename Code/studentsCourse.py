def academic_performance(student_id): # 6 assessments.txt, show feedback as well as per course_id
    try:
        with open("courses.txt", "r") as f:
            courses = {line.split(",")[0]: line.split(",")[1] for line in f.readlines()[1:]}

        with open("assessments.txt", "r") as f:
            assessments = [line.strip().split(",") for line in f.readlines()[1:]]

        with open("classes.txt", "r") as f:
            classes = {line.split(",")[0]: line.strip().split(",") for line in f.readlines()[1:]}

        print("\n========================= Academic Performance ========================")
        student_course_assessments = {}
        for assessment in assessments:
            if assessment[3] == student_id:
                course_id = assessment[1]
                if course_id not in student_course_assessments:
                    student_course_assessments[course_id] = []
                student_course_assessments[course_id].append(assessment)
                
        for course_id, assessments_list in student_course_assessments.items():
            course_name = courses.get(course_id, "Unknown Course")
            for assessment in assessments_list:
                class_id = assessment[2]
                print(f"\n{course_name} ({course_id}-{class_id})")
                print(f"{assessment[4]}") 
                print(f"Grade: {assessment[5]}")
                print(f"Lecturer's Note: {assessment[6]}")

    except FileNotFoundError:
        print("Data not found.")
    
    print("\n=========================================================================")
    print("0 | Previous Page")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourse(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")

def exam_schedule(student_id): # 5 examtimetable.txt, associate with course_id with student_id
    try:
        with open("course_enrollments.txt", "r") as f:
            enrollments = [line.strip().split(",") for line in f.readlines()[1:]]

        with open("classes.txt", "r") as f:
            classes = {line.split(",")[0]: line.strip().split(",") for line in f.readlines()[1:]}

        with open("courses.txt", "r") as f:
            courses = {line.split(",")[0]: line.split(",")[1] for line in f.readlines()[1:]}

        with open("examtimetable.txt", "r") as f:
            exam = [line.strip().split(",") for line in f.readlines()[1:]]

        exam_schedule_list = []

        print("\n========================= Exam Schedule ========================\n")
        for enrollment_data in enrollments:
            if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                class_id = enrollment_data[1]
                if class_id in classes:
                    course_id = classes[class_id][1]
                    course_name = courses.get(course_id)

                    for exam_data in exam:
                        if len(exam_data) > 2 and exam_data[1] == class_id and exam_data[2] == course_id:
                            exam_schedule_list.append({
                                'course_name': course_name,
                                'course_id': course_id,
                                'class_id': class_id,
                                'date': exam_data[3],
                                'time': f"{exam_data[4]} (GMT+8) - {exam_data[5]} (GMT+8)",
                                'location': exam_data[6]
                            })

        exam_schedule_list.sort(key=lambda x: x['date'])

        for exam_data in exam_schedule_list:
            print(f"{exam_data['date']}")
            print(f"{exam_data['course_name']} ({exam_data['course_id']}-{exam_data['class_id']})")
            print(f"{exam_data['time']}")
            print(f"{exam_data['location']} | CAMPUS")
            print(" ")
                    
    except FileNotFoundError:
        print("Data not found.")
        
    print("===============================================================")
    print("0 | Previous Page")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourse(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")

def schedule(student_id): # 4 classes.txt, associate with course_id with student_id
    try:
        with open("course_enrollments.txt", "r") as f:
            enrollments = [line.strip().split(",") for line in f.readlines()[1:]]

        with open("classes.txt", "r") as f:
            classes = {line.split(",")[0]: line.strip().split(",") for line in f.readlines()[1:]}

        with open("courses.txt", "r") as f:
            courses = {line.split(",")[0]: line.split(",")[1] for line in f.readlines()[1:]}
            
        with open("teachers.txt", "r") as f:
            teachers = {line.split(",")[0]: line.split(",")[1] for line in f.readlines()[1:]}

        print("\n========================= Class Schedule ========================\n")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            day_schedule = []
            for enrollment_data in enrollments:
                if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                    class_id = enrollment_data[1]
                    if class_id in classes:
                        classes_data = classes[class_id]
                        if classes_data[3] == day:
                            course_name = courses.get(classes_data[1])
                            teacher_name = teachers.get(classes_data[2])
                            day_schedule.append({
                                "start_time": f"{classes_data[4]}",
                                "end_time": f"{classes_data[5]}",
                                "course_name": course_name,
                                "course_id": classes_data[1],
                                "class_id": classes_data[0],
                                "location": classes_data[6],
                                "teacher_name": teacher_name
                            })
            if day_schedule:
                print(f"{day}")
                for class_info in sorted(day_schedule, key=lambda x: x["start_time"]):
                    print(f"\n{class_info['course_id']}-{class_info['class_id']}")
                    print(f"{class_info['course_name']}")
                    print(f"{class_info['start_time']} (GMT+8) - {class_info['end_time']} (GMT+8)")
                    print(f"{class_info['location']} | CAMPUS")
                    print(f"{class_info['teacher_name']}")
                    print(" ")
                    
    except FileNotFoundError:
        print("Data not found.")
        
    print("================================================================")
    print("0 | Previous Page")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourse(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")

def attendance(student_id): # 3 attendances.txt, associate with student_id and class_id but somehow need to associate with course_id from regstered courses by student.
    try:
        with open("course_enrollments.txt", "r") as f:
            enrollments = [line.strip().split(",") for line in f.readlines()[1:]]

        with open("classes.txt", "r") as f:
            classes = {line.split(",")[0]: line.strip().split(",") for line in f.readlines()[1:]}

        with open("courses.txt", "r") as f:
            courses = {line.split(",")[0]: line.split(",")[1] for line in f.readlines()[1:]}

        with open("attendances.txt", "r") as f:
            attendances = [line.strip().split(",") for line in f.readlines()[1:]]

        print("\n================== Attendance ==================\n")
        for enrollment_data in enrollments:
            if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                class_id = enrollment_data[1]
                if class_id in classes:
                    course_id = classes[class_id][1]
                    course_name = courses.get(course_id)
                    attended_classes = 0
                    total_classes = 0

                    for attendance_data in attendances:
                        if attendance_data[1] == class_id and attendance_data[2] == student_id:
                            total_classes += 1
                            if attendance_data[4] == "Present":
                                attended_classes += 1

                    print(f"{course_id}-{class_id}")                    
                    print(f"{course_name}") 
                    print(f"Classes: {attended_classes}/{total_classes}")
                    print(" ")

    except FileNotFoundError:
        print(f"Data not found.")

    print("========================================================")
    print("0 | Previous Page")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourse(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")

def enrollments(student_id): # 2 course_enrollments.txt, see the courses they are enrolled to
    try:
        with open("course_enrollments.txt", "r") as f:
            course_enrollments = f.readlines()[1:]

        with open("classes.txt", "r") as f:
            classes = f.readlines()[1:]

        print("\n============================ Enrolled Classes ===========================")
        for enrollment in course_enrollments:
            enrollment_data = enrollment.strip().split(",")
            if enrollment_data[2] == student_id and enrollment_data[4] == "Enrolled":
                class_id = enrollment_data[1]
                for classes_info in classes:
                    classes_data = classes_info.strip().split(",")
                    if classes_data[0] == class_id:
                        print(f"\n{classes_data[0]}-{classes_data[1]}")
                        print(f"{classes_data[7]}")
                        print(f"Status: {enrollment_data[4]}")
                        print(" ")
    except FileNotFoundError:
        print("Data not found.")
        
    print("=======================================================================")
    print("0 | Previous Page")
    while True:
        choice = input("")
        if choice == "0":
            studentsCourse(student_id)
            return
        else:
            print("Please try again and enter a valid choice.")

import random # for class_id

def next_enrollmentid(): # generates new course_enrollment_id
    try:
        with open("course_enrollments.txt", "r") as f:
            lines = f.readlines()
            if lines and len(lines) > 1:
                enrollment_id = [line.strip().split(",")[0] for line in lines[1:]]
                numeric_id = [int(e_id[2:]) for e_id in enrollment_id if e_id.startswith("CE") and e_id[2:].isdigit()]
                if numeric_id:
                    next_id = max(numeric_id) + 1
                    return f"CE{next_id:03d}"
            return "CE001"
    except FileNotFoundError:
        return "CE001"

def next_assessmentid(): # generates new assessment_id
    try:
        with open("course_enrollments.txt", "r") as f:
            lines = f.readlines()
            if lines and len(lines) > 1:  # Ensure there's more than just the header
                assessment_id = []
                for line in lines[1:]:
                    parts = line.strip().split(",")
                    if len(parts) > 3:
                        assessment_id.append(parts[3])
                numeric_id = [int(a_id[3:]) for a_id in assessment_id if a_id.startswith("ASM") and a_id[3:].isdigit()]
                if numeric_id:
                    next_id = max(numeric_id) + 1
                    return f"ASM{next_id:03d}"
            return "ASM001"
    except FileNotFoundError:
        return "ASM001"

def courses(student_details, student_id):
    print("============================ Available Courses ===========================")
    print(f"Student ID: {student_details[0]}\nStudent Name: {student_details[1]}")
    
    with open("courses.txt", "r") as f:
        lines = f.readlines()[1:]
        courses_data = [line.strip().split(",") for line in lines if line.strip()]

    headers = ["ID", "Course Name", "Info", "Instructor"]
    col_widths = [max(len(c[i]), len(headers[i])) + 2 for i in range(4) for c in courses_data]
    col_widths = col_widths[:4]
    col_widths[1] = max(len(headers[1]), 40)
    col_widths[2] = max(len(headers[2]), 60)
    
    print("=" * (sum(col_widths) + 9))
    print("  ".join(headers[i].ljust(col_widths[i]) for i in range(4)))
    print("=" * (sum(col_widths) + 9))

    for course in courses_data:
        print("  ".join(course[i].ljust(col_widths[i]) for i in range(4)))
        
    print("=" * (sum(col_widths) + 9))
    
    with open("courses.txt", "r") as f:
        lines = f.readlines()[1:]
        courses_data = [line.strip().split(",") for line in lines if line.strip()]

    headers = ["ID", "Course Name", "Info", "Instructor"]
    col_widths = [max(len(c[i]), len(headers[i])) + 2 for i in range(4) for c in courses_data]
    col_widths = col_widths[:4]
    col_widths[1] = max(len(headers[1]), 40)
    col_widths[2] = max(len(headers[2]), 60)
    
    print("=" * (sum(col_widths) + 9))
    print("  ".join(headers[i].ljust(col_widths[i]) for i in range(4)))
    print("=" * (sum(col_widths) + 9))

    for course in courses_data:
        print("  ".join(course[i].ljust(col_widths[i]) for i in range(4)))
        
    print("=" * (sum(col_widths) + 9))
    
    while True:
        choice = input("Would you like to enroll in a course? (y/n)\n")
        if choice.lower() == "y":
            course_id = input("Enter the ID (CXXX) of your preferred course: ")
            if course_id == "0":
                studentsCourse(student_id)
                return
            else:            
                with open("course_enrollments.txt", "r") as f:
                    enrollments = f.readlines()
                
                with open("classes.txt", "r") as f:
                    classes_data = [line.strip().split(",") for line in f.readlines()[1:] if line.strip()]

                available_class_ids = [c[0] for c in classes_data if c[1] == course_id]

                if not available_class_ids:
                    print("No classes available for this course.")
                    studentsCourse(student_id)
                    return
                
                class_id = available_class_ids[0] if available_class_ids else None
                
                if not class_id:
                    print("No classes available for enrollment.")
                    studentsCourse(student_id)
                    return

                enrolled = False # if the student is enrolled or unenrolled in the course
                unenrolled_index = -1
                for i, enrollment in enumerate(enrollments):
                    enrollment_data = enrollment.strip().split(",")
                    # Check if enrollment_data has at least 5 elements to avoid IndexError
                    if len(enrollment_data) >= 5 and enrollment_data[1] == class_id and enrollment_data[2] == student_id:
                        if enrollment_data[4] == "Enrolled":
                            print("You are already enrolled in this course. Please try a different course")
                            studentsCourse(student_id)
                            return
                        elif enrollment_data[4] == "Unenrolled":
                            unenrolled_index = i
                        enrolled = True
                        break

                if unenrolled_index != -1: # if student selected course "Unenrolled", update status to "Enrolled"
                    assessment_id = next_assessmentid()
                    enrollment_id = enrollments[unenrolled_index].strip().split(',')[0]
                    
                    with open("course_enrollments.txt", "w") as f:
                        for i, enrollment in enumerate(enrollments):
                            if i == unenrolled_index:
                                f.write(f"{enrollment_id},{class_id},{student_id},{assessment_id},Enrolled\n")
                            else:
                                f.write(enrollment)
                    print("You have successfully enrolled in the course.")
                    studentsCourse(student_id)
                    return

                elif not enrolled: # if student is not enrolled at all in file, create a new enrollment_id and write
                    new_enrollmentid = next_enrollmentid()
                    assessment_id = next_assessmentid()
                    
                    with open("course_enrollments.txt", "a") as f:
                        f.write(f"{new_enrollmentid},{class_id},{student_id},{assessment_id},Enrolled\n")
                    print("You have successfully enrolled in the course.")
                    studentsCourse(student_id)
                    return
        
        elif choice == "n":
            studentsCourse(student_id)
            return
        elif choice == "0":
            studentsCourse(student_id)
            return
        else:
            print("Please enter a valid choice.")
            
def studentsCourse(student_id):
    with open ("students.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == student_id:
                student_details = data
    
    print("\n======== Course Information ========")
    print(f"Student ID: {student_id}\nStudent Name: {student_details[1]}\nEnrollment Status: {student_details[6]}")
    print("====================================")
    print("|     1 | Available Courses        |")
    print("|     2 | Enrolled Courses         |")
    print("|     3 | Attendance               |")
    print("|     4 | Class Schedule           |")
    print("|     5 | Exam Schedule            |")
    print("|     6 | Academic Performance     |")
    print("|     0 | Previous Page            |")
    print("====================================")
    
    while True:
        choice = input("Please enter an option (0~6) : ")
        if choice == "1":
            courses(student_details, student_id)
            break
        elif choice == "2":
            enrollments(student_id)
        elif choice == "3":
            attendance(student_id)
        elif choice == "4":
            schedule(student_id)
        elif choice == "5":
            exam_schedule(student_id)
        elif choice == "6":
            academic_performance(student_id)
        elif choice == "0":
            import students
            students.students(student_id)
            return
        else:
            print("\nPlease try again and enter a valid choice.\n")