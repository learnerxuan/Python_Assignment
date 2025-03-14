"""This is a Staff's code."""

import staff_lib
import staff_color as color

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
    feedbacks, header = staff_lib.read_csv_file("../Data/feedbacks.txt")

    # Display table headers
    print("-" * 125)
    for column in header:
        print(f"{color.BOLD}{column.replace('_', ' ').upper():<20}{color.RESET}", end='')
    print()
    print("-" * 125)

    # Display only feedbacks related to the specified prefix (category)
    for feedback in feedbacks:
        if feedback["target_id"].startswith(prefix): 
            print("".join(f"{value:<20}" for value in feedback.values()))
            print("-" * 125)
    print()

    # Prompt user for feedback ID
    feedback_id = input(f"{color.GREEN}Enter feedback ID to reply (0 to cancel): {color.RESET}").strip()
    print()
    if feedback_id == "0":
        return 0  # Cancel operation
    
    # Validate feedback ID
    if not staff_lib.search_value("../Data/feedbacks.txt", 0, feedback_id):
        print(f"{color.RED}Invalid feedback ID.{color.RESET}\n")  # Notify user of invalid ID
        return 0
    
    # Find the selected feedback and prompt for a response
    for feedback in feedbacks:
        if feedback["feedback_id"] == feedback_id:
            response = input(f"{color.GREEN}Enter response (0 to cancel): {color.RESET}").strip()
            print()
            if response == "0":
                return 0  # Cancel operation
            feedback["response"] = response  # Store response in feedback record
    
    # Write updated feedback data back to file
    with open("../Data/feedbacks.txt", "w") as writer:
        writer.write(",".join(header) + "\n")  # Write header row
        for feedback in feedbacks:
            writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in feedback.values()) + "\n")
        print(f"{color.GREEN}Feedback replied successfully.{color.RESET}\n")  # Confirmation message
    
    return


def general_feedback():
    """Reply to general feedbacks."""
    try:
        print(f"{'=' * 53}{color.BOLD}{color.BLUE} GENERAL FEEDBACKS {color.RESET}{'=' * 53}")
        if reply_feedback("General") == 0:
            return  # If user cancels, exit function

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return


def course_feedback():
    """Reply to course-related feedbacks."""
    try:
        print(f"{'=' * 52}{color.BOLD}{color.BLUE} COURSE FEEDBACKS {color.RESET}{'=' * 53}")
        if reply_feedback("C") == 0:
            return  # If user cancels, exit function

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return
        

def teacher_feedback():
    """Reply to teacher-related feedbacks."""
    try:
        print(f"{'=' * 53}{color.BOLD}{color.BLUE} TEACHER FEEDBACKS {color.RESET}{'=' * 53}")
        if reply_feedback("T") == 0:
            return  # If user cancels, exit function

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return


def parents_contact():
    """Retrieve and display parents' contact information for a specific student."""
    try:
        print(f"{'=' * 54}{color.BOLD}{color.BLUE} PARENTS CONTACT {color.RESET}{'=' * 54}")
        student_id = input(f"{color.GREEN}Enter student ID (0 to cancel): {color.RESET}").strip()
        print()
        if student_id == "0":
            return  # Cancel operation
        
        # Search for the student's parent ID
        parents_id = staff_lib.search_value("../Data/parents.txt", 1, student_id, 0)
        if not parents_id:
            print(f"{color.RED}Parents not found.{color.RESET}\n")  # Notify user if no parents are found
            return

        # Retrieve and display parent details
        parents, header = staff_lib.read_csv_file("../Data/parents.txt")
        # Print table headers
        print("-" * 125)
        for column in header:
            print(f"{color.BOLD}{column.replace('_', ' ').upper():<20}{color.RESET}", end='')
        print()
        print("-" * 125)
        for parent in parents:
            if parent["parents_id"] == parents_id:
                # Print parent details
                print(" ".join(f"{value:<19}" for value in parent.values()))
                print("-" * 125)
        print()

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return


def contact_faculty():
    """Allow staff to input a faculty ID and send a message (simulation)."""
    try:
        print(f"{'=' * 18}{color.BOLD}{color.BLUE} CONTACT FACULTY {color.RESET}{'=' * 18}")
        # Read faculty data from file
        faculties, header = staff_lib.read_csv_file("../Data/faculties.txt")
        # Print table headers
        print("-" * 53)
        for column in header:
            print(f"{color.BOLD}{column.replace('_', ' ').upper():<15}{color.RESET}", end='')
        print()
        print("-" * 53)
        for faculty in faculties:
            # Display faculty information
            print(" ".join(f"{value:<15}" for value in faculty.values()))
            print("-" * 53) 
        print()

        # Prompt user for faculty ID
        while True:
            faculty_id = input(f"{color.GREEN}Enter faculty ID (0 to cancel): {color.RESET}").strip()
            print()
            if faculty_id == "0":
                return  # Cancel operation
            
            # Validate faculty ID
            if staff_lib.search_value("../Data/faculties.txt", 0, faculty_id):
                # Prompt user for message
                message = input(f"{color.GREEN}Enter message (0 to cancel): {color.RESET}").strip()
                print()
                if message == "0":
                    return  # Cancel operation
                print(f"{color.GREEN}Message sent.{color.RESET}\n")  # Confirmation message
                return
            print(f"{color.RED}Invalid faculty ID. Please try again.{color.RESET}\n")  # Notify user of invalid ID
            continue

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return
