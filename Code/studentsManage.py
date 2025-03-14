def emergencyChange(student_id):
    print("\n====== Modify Emergency Contact ======")
    while True:
        parents_name = input("Enter your emergency contact's name: ")  
        if parents_name == "0":
            return
        else:
            break
    
    while True:    
        phone_number = input("Enter your emergency contact's phone number: ")
        if phone_number == "0":
            return
        else:
            break
    
    while True:
        email = input("Enter the emergency contact's email: ")
        if email == "0":
            return
        else:
            break
        
    while True:
        gender = input("Enter the emergency contact's gender (Male/Female): ")
        if gender == "0":
            return
        elif gender == "Male" or gender == "Female":
            break
        else:
            print("\nPlease enter a valid input.")
            
    try:
        with open("parents.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: parents.txt file not found.")
        return

    updated_lines = []
    parent_id = None
    for line in lines:
        parts = line.strip().split(",")
        if parts[1] == student_id:
            parent_id = parts[0]
            updated_line = f"{parent_id},{student_id},{parents_name},{phone_number},{email},{gender}\n"
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    if parent_id is None:
        print(f"Error: No parent found for student ID {student_id}.")
        return

    with open("parents.txt", "w") as f:
        f.writelines(updated_lines)

    print(f"Emergency contact has been updated.")
    
    return

def phone_numberChange(student_id):
    print("\n====== Modify Phone Number ======")
    while True:
        phone_number = input("Enter your new phone number: ")
        if phone_number == "0":
            return
        else:
            break
        
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: students.txt file not found.")
        return

    updated_lines = []
    student_found = False
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == student_id:
            student_found = True
            updated_line = f"{parts[0]},{parts[1]},{parts[2]},{phone_number},{parts[4]},{parts[5]},{parts[6]},{parts[7]}\n"
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    if not student_found:
        print(f"No student found for current student ID.")
        return

    with open("students.txt", "w") as f:
        f.writelines(updated_lines)

    print(f"Your phone number has been updated.")
    return

def emailChange(student_id):
    print("\n====== Modify Email ======")
    
    while True:
        email = input("Enter your new email address: ")
        if email == "0":
            return
        else:
            break
    
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: students.txt file not found.")
        return

    updated_lines = []
    student_found = False
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == student_id:
            student_found = True
            updated_line = f"{parts[0]},{parts[1]},{parts[2]},{parts[3]},{email},{parts[5]},{parts[6]},{parts[7]}\n"
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    if not student_found:
        print(f"No student found for current student ID.")
        return

    with open("students.txt", "w") as f:
        f.writelines(updated_lines)

    print(f"Your email address has been updated.")
    return

def passwordChange(student_id):
    print("\n====== Change Password ======")
    while True:
        password = input("Enter your new password: ")
        if password == "0":
            return
        else:
            break
    while True:
        confirm_password = input("Confirm your new password: ")
        if confirm_password == "0":
            return
        else:
            break
    
    while True:
        if password != confirm_password:
            print("Error: Passwords do not match.")
            return
        else:
            break

    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: students.txt file not found.")
        return

    updated_lines = []
    student_found = False
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == student_id:
            student_found = True
            updated_line = f"{parts[0]},{parts[1]},{password},{parts[3]},{parts[4]},{parts[5]},{parts[6]},{parts[7]}\n"
            updated_lines.append(updated_line)
            print("Your password has been updated.")
        else:
            updated_lines.append(line)

    if not student_found:
        print(f"No student found for current student ID.")
        return

    with open("students.txt", "w") as f:
        f.writelines(updated_lines)
    
    return

def studentsManage(student_id): # MAIN MENU
    with open ("students.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == student_id:
                student_details = data
    with open ("parents.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == student_id:
                parents_details = data
        
    print("\n======== Account Management ========")
    print(f"Student ID: {student_id} \nStudent Name: {student_details[1]} \nPhone Number: {student_details[3]} \nEmail Address: {student_details[4]} \nGender: {student_details[4]}")
    print("====================================")
    print("|   1 | Change Password            |")
    print("|   2 | Update Email Address       |")
    print("|   3 | Update Phone Number        |")   
    print("|   4 | Update Emergency Contact   |")
    print("|   0 | Previous Page              |")
    print("====================================")
    while True:
        choice = input("Please enter an option (0~4) : ")
        if choice == "1":
            passwordChange(student_id)
        elif choice == "2":
            emailChange(student_id)
        elif choice == "3":
            phone_numberChange(student_id)
        elif choice == "4":
            emergencyChange(student_id)
        elif choice == "0":
            import students
            students.students(student_id)
            return
        else:
            print("\nPlease try again and enter a valid choice.\n")