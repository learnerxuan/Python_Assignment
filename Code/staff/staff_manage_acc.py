from choose import choose

def staff_manage_acc(staff_id, staff_name):
    print("""
1. Change Password
2. Update Phone Number
3. Update Email
0. Back""")
    
    choice = choose([0, 1, 2, 3])

    if choice == 1:
        staff_update_detail(staff_id, staff_name, "password")
    elif choice == 2:
        staff_update_detail(staff_id, staff_name, "phone")
    elif choice == 3:
        staff_update_detail(staff_id, staff_name, "email")
    elif choice == 0:
        import staff
        staff.staff(staff_id, staff_name)


def staff_update_detail(staff_id, staff_name, field):
    staffs = []
    staff_found = False
    try:
        with open("../../Data/staffs.txt", "r") as file:
            header = file.readline().split(",")
            for line in file:
                try:
                    id, name, password, phone, email, gender = line.strip().split(",")
                    staffs.append({"id": id, "name": name, "password": password, "phone": phone, "email": email, "gender": gender})
                except ValueError:
                    continue

        for staff in staffs:
            if staff["id"] == staff_id:
                staff_found = True
                while True:
                    new_detail = input(f"Enter new {field} (0 to cancel): ")
                    if new_detail == "0":
                        staff_manage_acc(staff_id, staff_name)
                        return

                    if field == "password":
                        confirm_detail = input("Confirm password: ")
                        if new_detail != confirm_detail:
                            print("Password does not match. Please try again.")
                            continue
                    staff[field] = new_detail
                    print(f"{field.capitalize()} updated successfully")
                    break

        if not staff_found:
            print("Staff not found. Please contact admin.")
            staff_manage_acc(staff_id, staff_name)
            return

        with open("../../Data/staffs.txt", "w") as writer:
            writer.write(",".join(header))
            for staff in staffs:
                writer.write(",".join(staff.values()) + "\n")
    
    except FileNotFoundError:
        print("File not found")
        staff_manage_acc(staff_id, staff_name)
        return
    
    staff_manage_acc(staff_id, staff_name)
    return
