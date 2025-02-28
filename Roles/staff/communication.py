import staff_lib


def communication():
    """Display feedback menu and processes user choices."""
    while True:
        print("""
1. General Feedbacks
2. Course Feedbacks
3. Teacher Feedbacks
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3])

        if choice == 1:
            general_feedback()
        elif choice == 2:
            course_feedback()
        elif choice == 3:
            teacher_feedback()
        elif choice == 0:
            # Return back to staff menu
            return


def reply_feedback(prefix):

    feedbacks, header = staff_lib.read_csv_file("./Data/feedbacks.txt")

    print(','.join(header))

    for feedback in feedbacks:
        if feedback["target_id"].startswith(prefix):
            print(','.join(feedback.values()))

    feedback_id = input("Enter feedback ID (0 to cancel): ").strip()
    if feedback_id == "0":
        return 0
    
    if not staff_lib.search_value("./Data/feedbacks.txt", 0, feedback_id):
        print("Invalid feedback ID.")
        return 0
    
    for feedback in feedbacks:
        if feedback["feedback_id"] == feedback_id:
            response = input("Enter response (0 to cancel): ")
            if response == "0":
                return 0
            feedback["response"] = response
    
    # Write newly changed data to file
    with open("./Data/feedbacks.txt", "w") as writer:
        writer.write(",".join(header) + "\n")
        for feedback in feedbacks:
            # Only write the value of each key-value pair for each resource
            writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in feedback.values()) + "\n")
        print(f"Feedback replied successfully.")
    
    return


def general_feedback():
    try:
        if reply_feedback("General") == 0:
            return

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def course_feedback():
    try:
        if reply_feedback("C") == 0:
            return

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return
        

def teacher_feedback():
    try:
        if reply_feedback("T") == 0:
            return

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return

