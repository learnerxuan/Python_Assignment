import color
import staff_lib


def staff_manage_acc(staff_id, staff_name):
    """Display staff manage account menu and processes user choices."""
    while True:
        print("""
1. Change Password
2. Update Phone Number
3. Update Email
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3])

        if choice == 1:
            field = "password"
        elif choice == 2:
            field = "phone"
        elif choice == 3:
            field = "email"
        elif choice == 0:
            # Return back to staff menu
            return

        staff_update_detail(staff_id, field)


def staff_update_detail(staff_id, field):
    """Updates the staff's personal detail based on the selected field."""

    # List to temporarily store all record from staffs.txt
    staffs = []
    
    # Flag to check if staff is found
    staff_found = False
    try:
        with open("../../Data/staffs.txt", "r") as file:
            header = file.readline().strip().split(",")
            for line in file:
                try:
                    # Pass the line (record) into staff_lib.read_csv_line and assign the return value (a list) into a variable
                    fields = staff_lib.read_csv_line(line.strip())

                    # Ignore the line if the line is not 6 fields
                    if len(fields) != 6:
                        continue

                    # Assign each element in the list to respective variable
                    id, name, password, phone, email, gender = fields

                    # Append each record as a dictionary
                    staffs.append({"id": id, "name": name, "password": password, "phone": phone, "email": email, "gender": gender})
                except ValueError:
                    continue
        
        # Search for user (staff) in file
        for staff in staffs:
            if staff["id"] == staff_id:
                staff_found = True
                while True:
                    new_detail = input(f"Enter new {field} (0 to cancel): ")

                    # Cancelled updating, return to staff_manage_acc
                    if new_detail == "0":
                        return

                    # Double confirm password
                    if field == "password":
                        confirm_detail = input("Confirm password: ")
                        if new_detail != confirm_detail:
                            print("Password does not match. Please try again.")
                            continue

                    # Assign new value of the updated field
                    staff[field] = new_detail
                    print(f"{field.capitalize()} updated successfully")
                    break

        if not staff_found:
            print("Staff not found. Please contact admin.")
            return

        # Write newly changed data to file
        with open("../../Data/staffs.txt", "w") as writer:
            writer.write(",".join(header) + "\n")
            for staff in staffs:
                # Only write the value of each key-value pair for each staff
                writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in staff.values()) + "\n")
    
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")
    
    # Return to staff_manage_acc after updating
    return
