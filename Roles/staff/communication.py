import staff_lib
import color

def communication():
    """Display feedback menu and process user choices."""
    while True:
        print(f"{'=' * 18}{color.BOLD}{color.BLUE} COMMUNICATION {color.RESET}{'=' * 18}")
        print(f"""{" " * 15}{color.YELLOW}1.{color.RESET} General Feedbacks
{" " * 15}{color.YELLOW}2.{color.RESET} Course Feedbacks
{" " * 15}{color.YELLOW}3.{color.RESET} Teacher Feedbacks
{" " * 15}{color.YELLOW}4.{color.RESET} Parents' Contacts
{" " * 15}{color.YELLOW}5.{color.RESET} Contact Faculty
{" " * 15}{color.YELLOW}0.{color.RESET} Back""")
        print(f"{'=' * 52}")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5])
        print()

        if choice == 1:
            general_feedback()
        elif choice == 2:
            course_feedback()
        elif choice == 3:
            teacher_feedback()
        elif choice == 4:
            parents_contact()
        elif choice == 5:
            contact_faculty()
        elif choice == 0:
            return  # Return to the previous menu


def reply_feedback(prefix):
    """Staff replies to feedbacks according to the type specified (field) by students."""

    # Read feedback data from file
    feedbacks, header = staff_lib.read_csv_file("./Data/feedbacks.txt")

    print(','.join(header))  # Display table headers

    # Display only feedbacks related to the specified prefix (category)
    for feedback in feedbacks:
        if feedback["target_id"].startswith(prefix): 
            print(','.join(feedback.values()))

    # Prompt user for feedback ID
    feedback_id = input("Enter feedback ID (0 to cancel): ").strip()
    if feedback_id == "0":
        return 0  # Cancel operation
    
    # Validate feedback ID
    if not staff_lib.search_value("./Data/feedbacks.txt", 0, feedback_id):
        print("Invalid feedback ID.")  # Notify user of invalid ID
        return 0
    
    # Find the selected feedback and prompt for a response
    for feedback in feedbacks:
        if feedback["feedback_id"] == feedback_id:
            response = input("Enter response (0 to cancel): ").strip()
            if response == "0":
                return 0  # Cancel operation
            feedback["response"] = response  # Store response in feedback record
    
    # Write updated feedback data back to file
    with open("./Data/feedbacks.txt", "w") as writer:
        writer.write(",".join(header) + "\n")  # Write header row
        for feedback in feedbacks:
            writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in feedback.values()) + "\n")
        print("Feedback replied successfully.")  # Confirmation message
    
    return


def general_feedback():
    """Reply to general feedbacks."""
    try:
        if reply_feedback("General") == 0:
            return  # If user cancels, exit function

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def course_feedback():
    """Reply to course-related feedbacks."""
    try:
        if reply_feedback("C") == 0:
            return  # If user cancels, exit function

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return
        

def teacher_feedback():
    """Reply to teacher-related feedbacks."""
    try:
        if reply_feedback("T") == 0:
            return  # If user cancels, exit function

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def parents_contact():
    """Retrieve and display parents' contact information for a specific student."""
    try:
        student_id = input("Enter student ID (0 to cancel): ").strip()
        if student_id == "0":
            return  # Cancel operation
        
        # Search for the student's parent ID
        parents_id = staff_lib.search_value("./Data/parents.txt", 1, student_id, 0)
        if not parents_id:
            print("Parents not found.")  # Notify user if no parents are found
            return

        # Retrieve and display parent details
        parents, header = staff_lib.read_csv_file("./Data/parents.txt")
        print(','.join(header))  # Print table headers
        for parent in parents:
            if parent["parents_id"] == parents_id:
                print(','.join(parent.values()))  # Print parent details

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def contact_faculty():
    """Allow staff to input a faculty ID and send a message (simulation)."""
    try:
        # Read faculty data from file
        faculties, header = staff_lib.read_csv_file("./Data/faculties.txt")
        print(",".join(header))  # Print table headers
        for faculty in faculties:
            print(",".join(faculty.values()))  # Display faculty information

        # Prompt user for faculty ID
        while True:
            faculty_id = input("Enter faculty ID (0 to cancel): ").strip()
            if faculty_id == "0":
                return  # Cancel operation
            
            # Validate faculty ID
            if staff_lib.search_value("./Data/faculties.txt", 0, faculty_id):
                # Prompt user for message
                message = input("Enter message (0 to cancel): ").strip()
                if message == "0":
                    return  # Cancel operation
                print("Message sent.")  # Confirmation message
                return
            print("Invalid faculty ID. Please try again.")  # Notify user of invalid ID
            continue

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return
