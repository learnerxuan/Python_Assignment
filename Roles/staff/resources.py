import staff_lib
from staff_lib import get_input

# Resource condition dictionary
resource_condition = {1: "Good", 2: "Used", 3: "Fair", 4: "Needs Repair"}


def resources():
    """Display resource management menu and processes user choices."""
    while True:
        print("""
1. View Resources
2. Add New Resource
3. Update Resource Details
4. Delete Resource
5. Split Resources
6. New Type
7. Maintenance Management
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6, 7])

        if choice == 1:
            view_resources()
        elif choice == 2:
            new_resources()
        elif choice == 3:
            update_resources()
        elif choice == 4:
            delete_resources()
        elif choice == 5:
            split_resources()
        elif choice == 6:
            new_type()
        elif choice == 7:
            maintenance()
        elif choice == 0:
            # Return back to staff menu
            return


def view_resources():
    """Display resource viewing menu and processes user choices."""
    while True:
        print("""
1. View All Resources
2. Search by ID
3. Search by Name
4. Filter by Type
5. Filter by Condition
6. Filter by Location
0. Back""")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6, 7])

        try:
            resources, header = staff_lib.read_csv_file("./Data/resources.txt")

            def get_resource(field, data):
                """This function search for resources according to user specified field"""
                found = False
                print(','.join(header))
                for resource in resources:
                    if resource[field].upper() == data:
                        print(','.join(resource.values()))
                        found = True
                if not found:
                    print("No matching records found.")

            # Print all resources
            if choice == 1:
                print(','.join(header))
                for resource in resources:
                    print(','.join(resource.values()))

            # Search by ID
            elif choice == 2:
                get_resource("resource_id", input("Enter resource ID: ").strip().upper())

            # Search by name
            elif choice == 3:
                get_resource("resource_name", input("Enter resource name: ").strip().upper())

            # Search by type
            elif choice == 4:
                with open("./Data/resource_type.txt", "r") as types:
                    print(''.join(types.readlines()))
                get_resource("resource_type", input("Enter resource type: ").strip().upper())
                    
            # Search by condition        
            elif choice == 5:
                print("1 - Good, 2 - Used, 3 - Fair, 4 - Needs Repair")
                while True:
                    try:
                        condition_num = int(get_input("Enter resource condition 1-4 (0 to cancel): "))
                        if condition_num not in resource_condition:
                            print("Invalid condition.")
                            continue
                        else:
                            get_resource("condition", resource_condition[condition_num].upper())
                            break
                    except ValueError:
                        continue
    
            # Search by location
            elif choice == 6:
                locations, _ = staff_lib.read_csv_file("./Data/locations.txt")
                for line in locations:
                    print(line["location_name"])
                get_resource("location", input("Enter location: ").strip().upper())

            elif choice == 0:
                # Return back to staff menu
                return
            
        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file") 

    return


def new_resources():
    """Register new resources, take name, condition, quantity, location"""

    try:
        # Get name
        resource_name = get_input("Enter resource name (0 to cancel): ")

        # User input resource type by choosing from the avialable list
        with open("./Data/resource_type.txt", "r") as types:
            print(''.join(types.readlines()))
        while True:
            resource_type = get_input("Enter resource type from above (0 to cancel): ").lower()
            if not staff_lib.search_value("./Data/resource_type.txt", 0, resource_type):
                print("Invalid resource type.")
                continue
            else:
                break
        
        # User input resource condition according their specified numbers
        print("1 - Good, 2 - Used, 3 - Fair, 4 - Needs Repair")
        while True:
            try:
                condition_num = int(get_input("Enter resource condition 1-4 (0 to cancel): "))
                if condition_num not in resource_condition:
                    print("Invalid condition.")
                    continue
                else:
                    condition = resource_condition[condition_num]
                    break
            except ValueError:
                continue
        
        # User input quantity, 0 is accepted
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        # User input location from a list of available locations
        loca, header = staff_lib.read_csv_file("./Data/locations.txt")
        print(header[0])
        for line in loca:
            print(line["location_name"])
        while True:
            location = get_input("Enter resource location (0 to cancel): ").title()
            if not staff_lib.search_value("./Data/locations.txt", 0, location):
                print("Invalid location.")
                continue
            else:
                break

        # Create new resource
        resource, head = staff_lib.read_csv_file("./Data/resources.txt")

        if resource:  # Check if the list is not empty
            last_id = resource[-1]["resource_id"]
            next_id = staff_lib.new_id(last_id, 1)  # Increment ID
        else: 
            next_id = "R001"  # Default starting ID if no records exist

        # Add new record
        with open("./Data/resources.txt", "a") as new_res:
            new_res.write(f"{next_id},{staff_lib.format_csv_value(resource_name)},{resource_type},{condition},{quantity},{staff_lib.format_csv_value(location)}\n")
        print("Successfully added!")

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def update_resources():
    """Update resource details"""
    while True:
        try:
            search_id = get_input("Enter resource ID (0 to cancel): ")
            if not staff_lib.search_value("./Data/resources.txt", 0, search_id):
                print("Invalid resource ID")
                continue
            
            print("""
1. Update name
2. Update type
3. Update condition
4. Update quantity
5. Update location
0. Back""")
            choice = staff_lib.choose([0, 1, 2, 3, 4, 5])

            if choice == 0:
                return
            elif choice == 1:
                field = "resource_name"
            elif choice == 2:
                field = "resource_type"
            elif choice == 3:
                field = "condition"
            elif choice == 4:
                field = "quantity"
            elif choice == 5:
                field = "location"

            resources, header = staff_lib.read_csv_file("./Data/resources.txt")

            for resource in resources:
                # Search for resource user wants to update
                if resource["resource_id"] == search_id:
                    if field == "resource_name":
                        new_detail = get_input("Enter new resource name (0 to cancel): ").title()

                    elif field == "resource_type":
                        # Display all type
                        with open("./Data/resource_type.txt", "r") as types:
                            print(''.join(types.readlines()))
                        while True:
                            # User input resource type by choosing from the avialable list
                            new_detail = get_input("Enter new resource type from above (0 to cancel): ").lower()
                            if not staff_lib.search_value("./Data/resource_type.txt", 0, new_detail): # Validate type
                                print("Invalid resource type.")
                                continue
                            else:
                                break
                    
                    elif field == "condition":
                        # User input resource condition according their specified numbers
                        print("1 - Good, 2 - Used, 3 - Fair, 4 - Needs Repair")
                        while True:
                            try:
                                condition_num = int(get_input("Enter new resource condition 1-4 (0 to cancel): "))
                                if condition_num not in resource_condition: # Validate condition
                                    print("Invalid condition.")
                                    continue
                                else:
                                    new_detail = resource_condition[condition_num]
                                    break
                            except ValueError:
                                continue    

                    elif field == "quantity":
                        # User input quantity, 0 is accepted
                        while True:
                            try:
                                new_detail = int(input("Enter new quantity: "))
                                break
                            except ValueError:
                                print("Please enter a valid number.")                    

                    elif field == "location":
                        # User input location from a list of available locations
                        loca, loca_header = staff_lib.read_csv_file("./Data/locations.txt")
                        print(loca_header[0])
                        for line in loca:
                            print(line["location_name"])
                        while True:
                            new_detail = get_input("Enter resource location (0 to cancel): ").title()
                            if not staff_lib.search_value("./Data/locations.txt", 0, new_detail):
                                print("Invalid location.")
                                continue
                            else:
                                break

                    resource[field] = new_detail
            
            # Write newly changed data to file
            with open("./Data/resources.txt", "w") as writer:
                writer.write(",".join(header) + "\n")
                for resource in resources:
                    # Only write the value of each key-value pair for each resource
                    writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in resource.values()) + "\n")
                print(f"{field.capitalize().replace("_", " ")} updated successfully.")
                break

        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file")
    return


def delete_resources():
    """Delete resource based on resource ID user inputted"""
    while True:
        try:
            resource_id = get_input("Enter resource ID (0 to cancel): ")
            # Validate the presence of resource ID
            if not staff_lib.search_value("./Data/resources.txt", 0, resource_id):
                print("Invalid resource ID.")
                continue
            
            resources, header = staff_lib.read_csv_file("./Data/resources.txt")

            # Append the list with all the other resource except the one user intends to delete
            resources = [resource for resource in resources if resource["resource_id"] != resource_id]

            # Write newly changed data to file
            with open("./Data/resources.txt", "w") as writer:
                writer.write(",".join(header) + "\n")
                for resource in resources:
                    # Only write the value of each key-value pair for each resource
                    writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in resource.values()) + "\n")
                print(f"Resource successfully deleted.")
                break

        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file")
    return


def split_resources():
    """Allows splitting of certain resource of a certain quantity become a new record and assign a new location"""
    while True:
        try:
            resource_id = get_input("Enter resource ID (0 to cancel): ")
            # Validate resource ID
            if not staff_lib.search_value("./Data/resources.txt", 0, resource_id):
                print("Invalid resource ID.")
                continue
            
            # Read resources into a list
            resources, header = staff_lib.read_csv_file("./Data/resources.txt")

            print(','.join(header))
            for resource in resources:
                if resource["resource_id"] == resource_id:
                    # Display the record
                    print(",".join(resource.values()))
                    while True:
                        try:
                            num_to_split = int(get_input("Enter quantity to be splitted out (0 to cancel): "))
                        except ValueError:
                            print("Invalid numbers.")
                            continue
                        
                        # Cannot split quantity more than the original
                        if num_to_split >= int(resource["quantity"]):
                            print("Number cannot exceed the original quantity.")
                            continue
                        
                        # User input new location from a list of available locations
                        loca, loca_header = staff_lib.read_csv_file("./Data/locations.txt")
                        print(loca_header[0])
                        for line in loca:
                            print(line["location_name"])
                        while True:
                            new_loc = get_input("Enter resource new location (0 to cancel): ").title()
                            if not staff_lib.search_value("./Data/locations.txt", 0, new_loc):
                                print("Invalid location.")
                                continue
                            else:
                                break

                        # Update original to the latest quantity
                        resource["quantity"] = str(int(resource["quantity"]) - num_to_split)

                        # Copy other old attribiutes to the newly splitted
                        new_name = resource["resource_name"]
                        new_type = resource["resource_type"]
                        new_cond = resource["condition"]
                        break

            # Create new record for the splitted
            splitted = {header[0]: staff_lib.new_id(resources[-1]["resource_id"], 1),
                        header[1]: new_name,
                        header[2]: new_type,
                        header[3]: new_cond,
                        header[4]: num_to_split,
                        header[5]: new_loc}
            
            # Append new record to the list
            resources.append(splitted)

            # Write newly changed data to file
            with open("./Data/resources.txt", "w") as writer:
                writer.write(",".join(header) + "\n")
                for resource in resources:
                    # Only write the value of each key-value pair for each resource
                    writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in resource.values()) + "\n")
                print(f"Resource successfully splitted.")
                break

        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file")
    
    return


def new_type():
    """Add new resource type"""

    with open("./Data/resource_type.txt", "a+") as types:
        print("Resource Type")
        types.seek(0)
        print(''.join(types.readlines()))

        new = get_input("Enter new type (0 to cancel): ").lower()

        # Check if resource type already existed
        if staff_lib.search_value("./Data/resource_type.txt", 0, new):
            print("Resource type exist")
            return
        
        types.writelines(new + "\n")
        print("New resource type added.")

    return


def maintenance():
    """Display maintenance management menu and processes user choices."""
    while True:
        print("""
1. Log maintenance
2. View maintenance history
3. Update maintenance status
4. Search maintenance record
5. Upcoming Maintenance Tasks
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6, 7])

        if choice == 1:
            log_maintenance()
        elif choice == 2:
            view_maintenance_history()
        elif choice == 3:
            update_maintrenance_status()
        elif choice == 4:
            search_maintenance()
        elif choice == 5:
            generate_maintenance_report()
        elif choice == 0:
            # Return back to staff menu
            return
        

def log_maintenance():
    ...