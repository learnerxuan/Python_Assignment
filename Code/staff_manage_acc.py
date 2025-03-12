"""This is a Staff's code."""

import staff_color as color
import staff_lib

def staff_manage_acc(staff_id, staff_name):
    """Display staff manage account menu and process user choices."""
    while True:
        print(f"{'=' * 17}{color.BOLD}{color.BLUE} MANAGE MY ACCOUNT {color.RESET}{'=' * 16}")
        print(f"""{" " * 15}{color.YELLOW}1.{color.RESET} Change Password
{" " * 15}{color.YELLOW}2.{color.RESET} Update Phone Number
{" " * 15}{color.YELLOW}3.{color.RESET} Update Email
{" " * 15}{color.YELLOW}0.{color.RESET} Back""")
        print(f"{'=' * 52}")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3])

        if choice == 1:
            field = "password"
        elif choice == 2:
            field = "phone_number"
        elif choice == 3:
            field = "email"
        elif choice == 0:
            return  # Return to staff menu

        staff_update_detail(staff_id, field)


def staff_update_detail(staff_id, field):
    """Updates the staff's personal detail based on the selected field."""

    try:
        staffs, header = staff_lib.read_csv_file("./Data/staffs.txt")

        # Flag to check if staff is found
        staff_found = False

        # Search for user (staff) in file
        for staff in staffs:
            if staff["staff_id"] == staff_id:
                staff_found = True
                print(f"\n{color.BOLD}Change {field.replace('_', ' ').title()}{color.RESET}\n")
                
                while True:
                    new_detail = input(f"Enter new {field.replace('_', ' ')} (0 to cancel): ").strip()
                    print()

                    # Cancelled updating, return to staff_manage_acc
                    if new_detail == "0":
                        return

                    # Double confirm password
                    if field == "password":
                        confirm_detail = input("Confirm password: ").strip()
                        print()
                        if new_detail != confirm_detail:
                            print(f"{color.YELLOW}Password does not match. Please try again.{color.RESET}\n")
                            continue

                    # Assign new value of the updated field
                    staff[field] = new_detail
                    print(f"{color.GREEN}{field.replace('_', ' ').title()} updated successfully.{color.RESET}\n")
                    break

        if not staff_found:
            print(f"{color.RED}Staff not found. Please contact admin.{color.RESET}\n")
            return

        # Write newly changed data to file
        with open("./Data/staffs.txt", "w") as writer:
            writer.write(",".join(header) + "\n")
            for staff in staffs:
                # Only write the value of each key-value pair for each staff
                writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in staff.values()) + "\n")

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    # Return to staff_manage_acc after updating
    return

