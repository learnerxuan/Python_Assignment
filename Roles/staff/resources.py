import staff_lib
import color

# Dictionary used in this file
resource_condition = {1: "Good", 2: "Used", 3: "Fair", 4: "Needs Repair"}
maintenance_types = {1: "Repair", 2: "Inspection", 3: "Replacement", 4: "Upgrade", 5: "Cleaning"}
maintenance_status = {1: "Completed", 2: "Pending", 3: "In Progress"}


def resources():
    """Display resource management menu and process user choices."""
    while True:
        print(f"{'=' * 16}{color.BOLD}{color.BLUE} RESOURCE MANAGEMENT {color.RESET}{'=' * 15}")
        print(f"""{" " * 13}{color.YELLOW}1.{color.RESET}  View Resources
{" " * 13}{color.YELLOW}2.{color.RESET}  Add New Resource
{" " * 13}{color.YELLOW}3.{color.RESET}  Update Resource Details
{" " * 13}{color.YELLOW}4.{color.RESET}  Delete Resource
{" " * 13}{color.YELLOW}5.{color.RESET}  Split Resources
{" " * 13}{color.YELLOW}6.{color.RESET}  New Type
{" " * 13}{color.YELLOW}7.{color.RESET}  Maintenance Management
{" " * 13}{color.YELLOW}0.{color.RESET}  Back""")
        print(f"{'=' * 52}")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6, 7])
        print()

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
            return  # Return to staff menu


def view_resources():
    """Display resource viewing menu and process user choices."""
    while True:
        print(f"{'=' * 18}{color.BOLD}{color.BLUE} VIEW RESOURCES {color.RESET}{'=' * 18}")
        print(f"""{" " * 12}{color.YELLOW}1.{color.RESET}  View All Resources
{" " * 12}{color.YELLOW}2.{color.RESET}  Search by ID
{" " * 12}{color.YELLOW}3.{color.RESET}  Search by Name
{" " * 12}{color.YELLOW}4.{color.RESET}  Filter by Type
{" " * 12}{color.YELLOW}5.{color.RESET}  Filter by Condition
{" " * 12}{color.YELLOW}6.{color.RESET}  Filter by Location
{" " * 12}{color.YELLOW}0.{color.RESET}  Back""")
        print(f"{'=' * 52}")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6])
        print()

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
                        condition_num = int(input("Enter resource condition 1-4 (0 to cancel): ").strip())
                        if condition_num == 0:
                            break
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
    """Register new resources, take name, condition, quantity, location."""

    try:
        # Get name
        resource_name = input("Enter resource name (0 to cancel): ").strip()

        if resource_name == "0":
            return

        # User input resource type by choosing from the avialable list
        with open("./Data/resource_type.txt", "r") as types:
            print(''.join(types.readlines()))
        while True:
            resource_type = input("Enter resource type from above (0 to cancel): ").strip().lower()
            
            if resource_type == "0":
                return

            if not staff_lib.search_value("./Data/resource_type.txt", 0, resource_type):
                print("Invalid resource type.")
                continue
            else:
                break
        
        # User input resource condition according their specified numbers
        print("1 - Good, 2 - Used, 3 - Fair, 4 - Needs Repair")
        while True:
            try:
                condition_num = int(input("Enter resource condition 1-4 (0 to cancel): ").strip())

                if condition_num == 0:
                    return

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
                quantity = int(input("Enter quantity: ").strip())
                break
            except ValueError:
                print("Please enter a valid number.")

        # User input location from a list of available locations
        loca, header = staff_lib.read_csv_file("./Data/locations.txt")
        print(header[0])
        for line in loca:
            print(line["location_name"])
        while True:
            location = input("Enter resource location (0 to cancel): ").strip().title()

            if location == "0":
                return

            if not staff_lib.search_value("./Data/locations.txt", 0, location):
                print("Invalid location.")
                continue
            else:
                break

        # Create new resource
        resource, _ = staff_lib.read_csv_file("./Data/resources.txt")

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
    """Update resource details."""
    while True:
        try:
            search_id = input("Enter resource ID (0 to cancel): ").strip()

            if search_id == "0":
                return

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
                        new_detail = input("Enter new resource name (0 to cancel): ").strip().title()

                        if new_detail == "0":
                            return

                    elif field == "resource_type":
                        # Display all type
                        with open("./Data/resource_type.txt", "r") as types:
                            print(''.join(types.readlines()))
                        while True:
                            # User input resource type by choosing from the avialable list
                            new_detail = input("Enter new resource type from above (0 to cancel): ").strip().lower()

                            if new_detail == "0":
                                return

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
                                condition_num = int(input("Enter new resource condition 1-4 (0 to cancel): ").strip())

                                if condition_num == 0:
                                    return

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
                                new_detail = int(input("Enter new quantity: ").strip())

                                if new_detail == 0:
                                    return

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
                            new_detail = input("Enter resource location (0 to cancel): ").strip().title()

                            if new_detail == 0:
                                return

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
    """Delete resource based on resource ID user inputted."""
    while True:
        try:
            resource_id = input("Enter resource ID (0 to cancel): ").strip()

            if resource_id == "0":
                return

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
    """Allows splitting of certain resource of a certain quantity become a new record and assign a new location."""
    while True:
        try:
            resource_id = input("Enter resource ID (0 to cancel): ").strip()

            if resource_id == "0":
                return

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
                            num_to_split = int(input("Enter quantity to be splitted out (0 to cancel): ").strip())

                            if num_to_split == 0:
                                return

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
                            new_loc = input("Enter resource new location (0 to cancel): ").sstrip().title()

                            if new_loc == "0":
                                return

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
    """Add new resource type."""
    try:
        with open("./Data/resource_type.txt", "a+") as types:
            print("Resource Type")
            types.seek(0)
            print(''.join(types.readlines()))

            new = input("Enter new type (0 to cancel): ").strip().lower()

            if new == "0":
                return

            # Check if resource type already existed
            if staff_lib.search_value("./Data/resource_type.txt", 0, new):
                print("Resource type exist")
                return
            
            types.writelines(new + "\n")
            print("New resource type added.")
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def maintenance():
    """Display maintenance management menu and process user choices."""
    while True:
        print(f"{'=' * 14}{color.BOLD}{color.BLUE} MAINTENANCE MANAGEMENT {color.RESET}{'=' * 14}")
        print(f"""{" " * 11}{color.YELLOW}1.{color.RESET}  Log Maintenance
{" " * 11}{color.YELLOW}2.{color.RESET}  View Maintenance History
{" " * 11}{color.YELLOW}3.{color.RESET}  Update Maintenance Status
{" " * 11}{color.YELLOW}4.{color.RESET}  Filter Maintenance Record
{" " * 11}{color.YELLOW}0.{color.RESET}  Back""")
        print(f"{'=' * 52}")

        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4])
        print()

        if choice == 1:
            log_maintenance()
        elif choice == 2:
            view_maintenance_history()
        elif choice == 3:
            update_maintenance_status()
        elif choice == 4:
            filter_maintenance()
        elif choice == 0:
            return  # Return to staff menu


def get_main_type():
    """Returns maintenance type in string."""
    print("Select Maintenance Type:")
    for key, value in maintenance_types.items():
        print(f"{key} - {value}")
    while True:
        try:
            type_num = int(input("Enter maintenance type (1-5) (0 to cancel): ").strip())
            if type_num == 0:
                return 0

            if type_num in maintenance_types:
                type = maintenance_types[type_num]
                return type
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue


def get_main_status():
    """Returns maintenance status in string."""

    print("Select Maintenance Status:")
    for key, value in maintenance_status.items():
        print(f"{key} - {value}")
    while True:
        try:
            status_num = int(input("Enter maintenance status (1-3) (0 to cancel): ").strip())
            if status_num == 0:
                return 0

            if status_num in maintenance_status:
                status = maintenance_status[status_num]
                return status
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 3.")


def log_maintenance():
    """Log new maintenance record."""
    try:
        while True:
            resource_id = input("Enter resource ID (0 to cancel): ").strip()

            if resource_id == "0":
                return

            # Check if resource ID exist
            if not staff_lib.search_value("./Data/resources.txt", 0, resource_id):
                print("Invalid resource.")
                continue
            break
        
        # Get date
        date = staff_lib.get_date()
        if date == "0":
            return
        
        # Get maintenance type
        type = get_main_type()
        if type == 0:
            return

        # Get cost
        while True:
            try:
                cost = float(input("Enter maintenance cost: ").strip())
                if cost < 0: # Prevent negative cost
                    print("Cost cannot be negative.")
                    continue
                cost = f"{cost:.2f}"  # Format to two decimal places
                break
            except ValueError:
                print("Invalid input. Please enter a valid number")

        # Get maintenance status
        status = get_main_status()
        if status == 0:
            return

        # Enter additional notes
        notes = input("Enter notes (0 to cancel): ").strip()
        if notes == "0":
            return
        notes = staff_lib.format_csv_value(notes)

        # Create new maintenance log
        maintenance, _ = staff_lib.read_csv_file("./Data/maintenances.txt")

        if maintenance:  # Check if the list is not empty
            last_id = maintenance[-1]["maintenance_id"]
            next_id = staff_lib.new_id(last_id, 1)  # Increment ID
        else: 
            next_id = "R001"  # Default starting ID if no records exist

        # Add new record
        with open("./Data/maintenances.txt", "a") as new_main:
            new_main.write(f"{next_id},{resource_id},{date},{type},{cost},{status},{notes}\n")
        print("Successfully added!")

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def view_maintenance_history():
    """View maintenance history of a specific resource."""
    try:
        # Search for resource ID
        resource_id = input("Enter resource ID (0 to cancel): ").strip()

        if resource_id == "0":
            return
        
        # If resource ID exist in maintenances.txt, returns a list for multiple occurance, single value for one occurance
        main_ids = staff_lib.search_value("./Data/maintenances.txt", 1, resource_id, 0)

        if main_ids == False:
            print("Resource has no maintenance history.")
            return

        maintenances, header = staff_lib.read_csv_file("./Data/maintenances.txt") 
        print(",".join(header))

        # If there's only one occurance
        if isinstance(main_ids, str):
            for maintenance in maintenances:
                if maintenance["maintenance_id"] == main_ids:
                    print(",".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()))

        elif isinstance(main_ids, list):
            # Iterate over a list of maintenance ID for that one resource
            for main_id in main_ids:
                for maintenance in maintenances:
                    if maintenance["maintenance_id"] == main_id:
                        print(",".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()))

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return


def update_maintenance_status():
    """Update maintenance status of a specific maintenance record."""
    try:
        maintenance_id = input("Enter maintenance ID: ").strip()
        if not staff_lib.search_value("./Data/maintenances.txt", 0, maintenance_id):
            print("Invalid maintenance ID.")
            return
        maintenances, header = staff_lib.read_csv_file("./Data/maintenances.txt")
        for maintenance in maintenances:
            if maintenance["maintenance_id"] == maintenance_id:
                # Output the maintenance record
                print(",".join(header))
                print(",".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()))

                # Get new maintenance status
                status = get_main_status()
                if status == 0:
                    return

                # Update the status of the specific record
                maintenance["status"] = status

        # Write newly changed data to file
        with open("./Data/maintenances.txt", "w") as writer:
            writer.write(",".join(header) + "\n")
            for maintenance in maintenances:
                # Only write the value of each key-value pair for each maintenance
                writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()) + "\n")
            print(f"Maintenance status successfully updated.")

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")

    return
    

def filter_maintenance():
    """Display maintenance records of a specific type or status."""
    while True:
        try:
            print("1. Filter by type\n2. Filter by status\n0. Back")
            # Get field that user wants to filter by
            choice = staff_lib.choose([0, 1, 2])
            if choice == 0:
                return
            
            # Filter by type
            elif choice == 1:
                type = get_main_type()
                if type == 0:
                    return
                
                # Get the maintenance IDs of the specific type
                maintenance_ids = staff_lib.search_value("./Data/maintenances.txt", 3, type, 0)

                if maintenance_ids == False:
                    print("No record.")
                    continue
                
                maintenances, header = staff_lib.read_csv_file("./Data/maintenances.txt")

                print(",".join(header))

                # Iterate throught the list of all maintenances
                for maintenance in maintenances:
                    # Print the specific type only
                    if maintenance["type"] == type:
                        print(",".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()))

            # Filter by status
            elif choice == 2:
                status = get_main_status()
                if status == 0:
                    return
                
                # Get the maintenance IDs of the specific status
                maintenance_ids = staff_lib.search_value("./Data/maintenances.txt", 5, status, 0)

                if maintenance_ids == False:
                    print("No record.")
                    continue
                
                maintenances, header = staff_lib.read_csv_file("./Data/maintenances.txt")

                print(",".join(header))

                # Iterate throught the list of all maintenances
                for maintenance in maintenances:
                    # Print the specific status only
                    if maintenance["status"] == status:
                        print(",".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()))

        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file")
        return
