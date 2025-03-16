"""This is a Staff's code."""

import staff_lib
import staff_color as color


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

    resource_condition = {1: "Good", 2: "Used", 3: "Fair", 4: "Needs Repair"}

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

        try:
            resources, header = staff_lib.read_csv_file("../Data/resources.txt")

            def get_resource(field, data):
                """This function search for resources according to user specified field"""
                print()
                found = False
                print("-" * 125)
                for column in header:
                    print(f"{color.BOLD}{column.replace('_', ' ').upper():<20}{color.RESET}", end='')
                print()
                print("-" * 125)
                for resource in resources:
                    if resource[field].upper() == data:
                        print("".join(f"{value:<20}" for value in resource.values()))
                        print("-" * 125)
                        found = True
                print()
                if not found:
                    print(f"{color.RED}No matching records found.{color.RESET}")

            # Print all resources
            if choice == 1:
                print(f"{color.YELLOW}All Resources:{color.RESET}")
                print("-" * 125)
                for column in header:
                    print(f"{color.BOLD}{column.replace('_', ' ').upper():<20}{color.RESET}", end='')
                print()
                print("-" * 125)
                for resource in resources:
                    print("".join(f"{value:<20}" for value in resource.values()))
                print("-" * 125)
                print()

            # Search by ID
            elif choice == 2:
                get_resource("resource_id", input(f"{color.GREEN}Enter resource ID: {color.RESET}").strip().upper())

            # Search by name
            elif choice == 3:
                get_resource("resource_name", input(f"{color.GREEN}Enter resource name: {color.RESET}").strip().upper())

            # Search by type
            elif choice == 4:
                with open("../Data/resource_type.txt", "r") as types:
                    print(''.join(types.readlines()), end="")
                get_resource("resource_type", input(f"{color.GREEN}Enter resource type: {color.RESET}").strip().upper())
                    
            # Search by condition        
            elif choice == 5:
                print(f"{color.YELLOW}Condition:\n{color.RESET}1 - Good\n2 - Used\n3 - Fair\n4 - Needs Repair")
                while True:
                    try:
                        condition_num = int(input(f"{color.GREEN}Enter resource condition 1-4 (0 to cancel): {color.RESET}").strip())
                        if condition_num == 0:
                            break
                        if condition_num not in resource_condition:
                            print(f"Invalid condition.")
                            continue
                        else:
                            get_resource("condition", resource_condition[condition_num].upper())
                            break
                    except ValueError:
                        continue
    
            # Search by location
            elif choice == 6:
                locations, _ = staff_lib.read_csv_file("../Data/locations.txt")
                print(f"{color.YELLOW}Locations:{color.RESET}")
                for line in locations:
                    print(line["location_name"])
                get_resource("location", input(f"{color.GREEN}Enter location: {color.RESET}").strip().upper())

            elif choice == 0:
                # Return back to staff menu
                return
            
        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n") 

    return


def new_resources():
    """Register new resources, take name, condition, quantity, location."""

    resource_condition = {1: "Good", 2: "Used", 3: "Fair", 4: "Needs Repair"}

    try:
        print(f"{'=' * 30}{color.BOLD}{color.BLUE} ADD NEW RESOURCE {color.RESET}{'=' * 30}")

        # Get name
        resource_name = input(f"{color.GREEN}Enter resource name (0 to cancel): {color.RESET}").strip()
        print()

        if resource_name == "0":
            return

        # User input resource type by choosing from the avialable list
        with open("../Data/resource_type.txt", "r") as types:
            print(f"{color.YELLOW}Resource types:{color.RESET}")
            print(''.join(types.readlines()), end='')
        while True:
            resource_type = input(f"{color.GREEN}Enter resource type from above (0 to cancel): {color.RESET}").strip().lower()
            print()
            
            if resource_type == "0":
                return

            if not staff_lib.search_value("../Data/resource_type.txt", 0, resource_type):
                print(f"{color.RED}Invalid resource type.{color.RESET}")
                print()
                continue
            else:
                break
        
        # User input resource condition according their specified numbers
        print(f"{color.YELLOW}Resource Condition:{color.RESET}")
        print("1 - Good\n2 - Used\n3 - Fair\n4 - Needs Repair")
        while True:
            try:
                condition_num = int(input(f"{color.GREEN}Enter resource condition 1-4 (0 to cancel): {color.RESET}").strip())
                print()

                if condition_num == 0:
                    return

                if condition_num not in resource_condition:
                    print(f"{color.RED}Invalid condition.{color.RESET}")
                    print()
                    continue
                else:
                    condition = resource_condition[condition_num]
                    break
            except ValueError:
                continue
        
        # User input quantity, 0 is accepted
        while True:
            try:
                quantity = int(input(f"{color.GREEN}Enter quantity: {color.RESET}").strip())
                print()
                break
            except ValueError:
                print(f"{color.GREEN}Please enter a valid number.{color.RESET}")

        # User input location from a list of available locations
        loca, header = staff_lib.read_csv_file("../Data/locations.txt")
        print(f"{color.YELLOW}Locations:{color.RESET}")
        print(header[0])
        for line in loca:
            print(line["location_name"])
        while True:
            location = input(f"{color.GREEN}Enter resource location (0 to cancel): {color.RESET}").strip().title()
            print()

            if location == "0":
                return

            if not staff_lib.search_value("../Data/locations.txt", 0, location):
                print(f"{color.RED}Invalid location.{color.RED}")
                print()
                continue
            else:
                break

        # Create new resource
        resource, _ = staff_lib.read_csv_file("../Data/resources.txt")

        if resource:  # Check if the list is not empty
            last_id = resource[-1]["resource_id"]
            next_id = staff_lib.new_id(last_id, 1)  # Increment ID
        else: 
            next_id = "R001"  # Default starting ID if no records exist

        # Add new record
        with open("../Data/resources.txt", "a") as new_res:
            new_res.write(f"{next_id},{staff_lib.format_csv_value(resource_name)},{resource_type},{condition},{quantity},{staff_lib.format_csv_value(location)}\n")
        print(f"{color.GREEN}Successfully added!{color.RESET}")
        print()

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    return


def update_resources():
    """Update resource details."""

    resource_condition = {1: "Good", 2: "Used", 3: "Fair", 4: "Needs Repair"}

    while True:
        try:
            print(f"{'=' * 20}{color.BOLD}{color.BLUE} UPDATE RESOURCE DETAILS {color.RESET}{'=' * 20}")
            search_id = input(f"{color.GREEN}Enter resource ID (0 to cancel): {color.RESET}").strip()
            print()

            if search_id == "0":
                return

            if not staff_lib.search_value("../Data/resources.txt", 0, search_id):
                print(f"{color.RED}Invalid resource ID{color.RESET}\n")
                continue
            
            print(f"""{" " * 20}{color.YELLOW}1.{color.RESET} Update name
{" " * 20}{color.YELLOW}2.{color.RESET} Update type
{" " * 20}{color.YELLOW}3.{color.RESET} Update condition
{" " * 20}{color.YELLOW}4.{color.RESET} Update quantity
{" " * 20}{color.YELLOW}5.{color.RESET} Update location
{" " * 20}{color.YELLOW}0.{color.RESET} Back\n""")
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

            resources, header = staff_lib.read_csv_file("../Data/resources.txt")

            for resource in resources:
                # Search for resource user wants to update
                if resource["resource_id"] == search_id:
                    if field == "resource_name":
                        new_detail = input(f"{color.GREEN}Enter new resource name (0 to cancel): {color.RESET}").strip().title()
                        print()

                        if new_detail == "0":
                            return

                    elif field == "resource_type":
                        # Display all type
                        with open("../Data/resource_type.txt", "r") as types:
                            print(f"{color.YELLOW}Resource types:{color.RESET}")
                            print(''.join(types.readlines()))
                        while True:
                            # User input resource type by choosing from the avialable list
                            new_detail = input(f"{color.GREEN}Enter new resource type from above (0 to cancel): {color.RESET}").strip().lower()
                            print()
                            if new_detail == "0":
                                return

                            if not staff_lib.search_value("../Data/resource_type.txt", 0, new_detail): # Validate type
                                print(f"{color.RED}Invalid resource type.{color.RESET}\n")
                                continue
                            else:
                                break
                    
                    elif field == "condition":
                        # User input resource condition according their specified numbers
                        print(f"{color.YELLOW}Resource Condition:{color.RESET}")
                        print("1 - Good\n2 - Used\n3 - Fair\n4 - Needs Repair")
                        while True:
                            try:
                                condition_num = int(input(f"{color.GREEN}Enter new resource condition 1-4 (0 to cancel): {color.RESET}").strip())

                                if condition_num == 0:
                                    return

                                if condition_num not in resource_condition: # Validate condition
                                    print(f"{color.RED}Invalid condition.{color.RESET}\n")
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
                                new_detail = int(input(f"{color.GREEN}Enter new quantity: {color.RESET}").strip())
                                print()

                                if new_detail == 0:
                                    return

                                break
                            except ValueError:
                                print(f"{color.RED}Please enter a valid number.{color.RESET}")                    

                    elif field == "location":
                        # User input location from a list of available locations
                        loca, loca_header = staff_lib.read_csv_file("../Data/locations.txt")
                        print(f"{color.BOLD}{loca_header[0].replace("_", " ").upper()}{color.RESET}")
                        for line in loca:
                            print(line["location_name"])
                        while True:
                            new_detail = input(f"{color.GREEN}Enter resource location (0 to cancel): {color.RESET}").strip().title()
                            print()

                            if new_detail == "0":
                                return

                            if not staff_lib.search_value("../Data/locations.txt", 0, new_detail):
                                print(f"{color.RED}Invalid location.{color.RESET}\n")
                                continue
                            else:
                                break

                    resource[field] = new_detail
            
            # Write newly changed data to file
            with open("../Data/resources.txt", "w") as writer:
                writer.write(",".join(header) + "\n")
                for resource in resources:
                    # Only write the value of each key-value pair for each resource
                    writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in resource.values()) + "\n")
                print(f"{field.capitalize().replace("_", " ")} updated successfully.")
                break

        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    return


def delete_resources():
    """Delete resource based on resource ID user inputted."""
    while True:
        try:
            print(f"{'=' * 20}{color.BLUE} DELETE RESOURCE {color.RESET}{'=' * 20}")
            resource_id = input(f"{color.GREEN}Enter resource ID (0 to cancel): {color.RESET}").strip()
            print()

            if resource_id == "0":
                return

            # Validate the presence of resource ID
            if not staff_lib.search_value("../Data/resources.txt", 0, resource_id):
                print(f"{color.RED}Invalid resource ID.{color.RESET}\n")
                continue
            
            resources, header = staff_lib.read_csv_file("../Data/resources.txt")

            # Append the list with all the other resource except the one user intends to delete
            resources = [resource for resource in resources if resource["resource_id"] != resource_id]

            # Write newly changed data to file
            with open("../Data/resources.txt", "w") as writer:
                writer.write(",".join(header) + "\n")
                for resource in resources:
                    # Only write the value of each key-value pair for each resource
                    writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in resource.values()) + "\n")
                print(f"{color.GREEN}Resource successfully deleted.{color.RESET}\n")
                break

        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    return


def split_resources():
    """Allows splitting of certain resource of a certain quantity become a new record and assign a new location."""
    while True:
        try:
            print(f"{'=' * 54}{color.BLUE} SPLIT RESOURCES {color.RESET}{'=' * 54}")
            resource_id = input(f"{color.GREEN}Enter resource ID (0 to cancel): {color.RESET}").strip()
            print()

            if resource_id == "0":
                return

            # Validate resource ID
            if not staff_lib.search_value("../Data/resources.txt", 0, resource_id):
                print(f"{color.RED}Invalid resource ID.{color.RESET}\n")
                continue
            
            # Read resources into a list
            resources, header = staff_lib.read_csv_file("../Data/resources.txt")

            print("-" * 125)
            for column in header:
                print(f"{color.BOLD}{column.replace('_', ' ').upper():<20}{color.RESET}", end='')
            print()
            print("-" * 125)

            for resource in resources:
                if resource["resource_id"] == resource_id:
                    # Display the record
                    print("".join(f"{value:<20}" for value in resource.values()))
                    print("-" * 125)
                    while True:
                        try:
                            num_to_split = int(input(f"{color.GREEN}Enter quantity to be splitted out (0 to cancel): {color.RESET}").strip())
                            print()

                            if num_to_split == 0:
                                return

                        except ValueError:
                            print(f"{color.RED}Invalid numbers.{color.RESET}\n")
                            continue
                        
                        # Cannot split quantity more than the original
                        if num_to_split >= int(resource["quantity"]):
                            print(f"{color.RED}Number cannot exceed the original quantity.{color.RESET}\n")
                            continue
                        
                        # User input new location from a list of available locations
                        loca, loca_header = staff_lib.read_csv_file("../Data/locations.txt")
                        print(f"{color.BOLD}{loca_header[0].replace("_", " ").upper()}{color.RESET}")
                        for line in loca:
                            print(line["location_name"])
                        while True:
                            new_loc = input(f"{color.GREEN}Enter resource new location (0 to cancel): {color.RESET}").strip().title()
                            print()

                            if new_loc == "0":
                                return

                            if not staff_lib.search_value("../Data/locations.txt", 0, new_loc):
                                print(f"{color.RED}Invalid location.{color.RESET}\n")
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
            with open("../Data/resources.txt", "w") as writer:
                writer.write(",".join(header) + "\n")
                for resource in resources:
                    # Only write the value of each key-value pair for each resource
                    writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in resource.values()) + "\n")
                print(f"{color.GREEN}Resource successfully splitted.{color.RESET}\n")
                break

        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    
    return


def new_type():
    """Add new resource type."""
    try:
        with open("../Data/resource_type.txt", "a+") as types:
            print(f"{color.YELLOW}Existing Resource Type:{color.RESET}")
            types.seek(0)
            print(''.join(types.readlines()), end="")

            new = input(f"{color.GREEN}Enter new type (0 to cancel): {color.RESET}").strip().lower()
            print()

            if new == "0":
                return

            # Check if resource type already existed
            if staff_lib.search_value("../Data/resource_type.txt", 0, new):
                print(f"{color.RED}Resource type exist.{color.RESET}\n")
                return
            
            types.writelines(new + "\n")
            print(f"{color.GREEN}New resource type added.{color.RESET}")
    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

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

    maintenance_types = {1: "Repair", 2: "Inspection", 3: "Replacement", 4: "Upgrade", 5: "Cleaning"}

    print(f"{color.YELLOW}Select Maintenance Type:{color.RESET}")
    for key, value in maintenance_types.items():
        print(f"{key} - {value}")
    while True:
        try:
            type_num = int(input(f"{color.GREEN}Enter maintenance type (1-5) (0 to cancel): {color.RESET}").strip())
            print()
            if type_num == 0:
                return 0

            if type_num in maintenance_types:
                type = maintenance_types[type_num]
                return type
            else:
                print(f"{color.RED}Invalid choice. Please enter a number between 1 and 5.{color.RESET}\n")
        except ValueError:
            print(f"{color.RED}Invalid choice. Please enter a number between 1 and 5.{color.RESET}\n")
            continue


def get_main_status():
    """Returns maintenance status in string."""

    maintenance_status = {1: "Completed", 2: "Pending", 3: "In Progress"}

    print(f"{color.YELLOW}Select Maintenance Status:{color.RESET}")
    for key, value in maintenance_status.items():
        print(f"{key} - {value}")
    while True:
        try:
            status_num = int(input(f"{color.GREEN}Enter maintenance status (1-3) (0 to cancel): {color.RESET}").strip())
            print()
            if status_num == 0:
                return 0

            if status_num in maintenance_status:
                status = maintenance_status[status_num]
                return status
            else:
                print(f"{color.RED}Invalid choice. Please enter a number between 1 and 3.{color.RESET}\n")
        except ValueError:
            print(f"{color.RED}Invalid choice. Please enter a number between 1 and 3.{color.RESET}\n")


def log_maintenance():
    """Log new maintenance record."""
    try:
        while True:
            print(f"{'=' * 20}{color.BOLD}{color.BLUE} LOG MAINTENANCE {color.RESET}{'=' * 20}")
            resource_id = input(f"{color.GREEN}Enter resource ID (0 to cancel): {color.RESET}").strip()
            print()

            if resource_id == "0":
                return

            # Check if resource ID exist
            if not staff_lib.search_value("../Data/resources.txt", 0, resource_id):
                print(f"{color.RED}Invalid resource.{color.RESET}\n")
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
                cost = float(input(f"{color.GREEN}Enter maintenance cost: {color.RESET}").strip())
                if cost < 0: # Prevent negative cost
                    print(f"{color.RED}Cost cannot be negative.{color.RESET}\n")
                    continue
                cost = f"{cost:.2f}"  # Format to two decimal places
                break
            except ValueError:
                print(f"{color.RED}Invalid input. Please enter a valid number{color.RESET}\n")

        # Get maintenance status
        status = get_main_status()
        if status == 0:
            return

        # Enter additional notes
        notes = input(f"{color.GREEN}Enter notes (0 to cancel): {color.RESET}").strip()
        print()
        if notes == "0":
            return
        notes = staff_lib.format_csv_value(notes)

        # Create new maintenance log
        maintenance, _ = staff_lib.read_csv_file("../Data/maintenances.txt")

        if maintenance:  # Check if the list is not empty
            last_id = maintenance[-1]["maintenance_id"]
            next_id = staff_lib.new_id(last_id, 1)  # Increment ID
        else: 
            next_id = "R001"  # Default starting ID if no records exist

        # Add new record
        with open("../Data/maintenances.txt", "a") as new_main:
            new_main.write(f"{next_id},{resource_id},{date},{type},{cost},{status},{notes}\n")
        print(f"{color.GREEN}Successfully added!{color.RESET}\n")

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return


def view_maintenance_history():
    """View maintenance history of a specific resource."""
    try:
        print(f"{'=' * 49}{color.BOLD}{color.BLUE} VIEW MAINTENANCE HISTORY {color.RESET}{'=' * 50}")
        # Search for resource ID
        resource_id = input(f"{color.GREEN}Enter resource ID (0 to cancel): {color.RESET}").strip()
        print()

        if resource_id == "0":
            return
        
        # If resource ID exist in maintenances.txt, returns a list for multiple occurance, single value for one occurance
        main_ids = staff_lib.search_value("../Data/maintenances.txt", 1, resource_id, 0)

        if main_ids == False:
            print(f"{color.RED}Resource has no maintenance history.{color.RESET}\n")
            return

        maintenances, header = staff_lib.read_csv_file("../Data/maintenances.txt") 
        print("-" * 125)
        for column in header:
            print(f"{color.BOLD}{column.replace('_', ' ').upper():<15}{color.RESET}", end='')
        print()
        print("-" * 125)

        # If there's only one occurance
        if isinstance(main_ids, str):
            for maintenance in maintenances:
                if maintenance["maintenance_id"] == main_ids:
                    print(f"".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()))
                    print("-" * 125)
            print()

        elif isinstance(main_ids, list):
            # Iterate over a list of maintenance ID for that one resource
            for main_id in main_ids:
                for maintenance in maintenances:
                    if maintenance["maintenance_id"] == main_id:
                        print(f"".join(staff_lib.format_csv_value(str(f"{value:<15}")) for value in maintenance.values()))
                        print("-" * 125)
            print()

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")

    return


def update_maintenance_status():
    """Update maintenance status of a specific maintenance record."""
    try:
        print(f"{'=' * 49}{color.BOLD}{color.BLUE} UPDATE MAINTENANCE STATUS {color.RESET}{'=' * 50}")
        maintenance_id = input(f"{color.GREEN}Enter maintenance ID: {color.RESET}").strip()
        print()
        if not staff_lib.search_value("../Data/maintenances.txt", 0, maintenance_id):
            print(f"{color.RED}Invalid maintenance ID.{color.RESET}\n")
            return
        maintenances, header = staff_lib.read_csv_file("../Data/maintenances.txt")
        for maintenance in maintenances:
            if maintenance["maintenance_id"] == maintenance_id:
                # Output the maintenance record
                print("-" * 125)
                for column in header:
                    print(f"{color.BOLD}{column.replace('_', ' ').upper():<15}{color.RESET}", end='')
                print()
                print("-" * 125)
                print(f"".join(staff_lib.format_csv_value(str(f"{value:<15}")) for value in maintenance.values()))
                print("-" * 125)
                print()

                # Get new maintenance status
                status = get_main_status()
                if status == 0:
                    return

                # Update the status of the specific record
                maintenance["status"] = status

        # Write newly changed data to file
        with open("../Data/maintenances.txt", "w") as writer:
            writer.write(",".join(header) + "\n")
            for maintenance in maintenances:
                # Only write the value of each key-value pair for each maintenance
                writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in maintenance.values()) + "\n")
            print(f"{color.GREEN}Maintenance status successfully updated.{color.RESET}\n")

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    return
    

def filter_maintenance():
    """Display maintenance records of a specific type or status."""
    while True:
        try:
            print(f"{'=' * 49}{color.BOLD}{color.BLUE} FILTER MAINTENANCE RECORD {color.RESET}{'=' * 49}")
            print(f"{color.YELLOW}Option:{color.RESET}\n1. Filter by type\n2. Filter by status\n0. Back")
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
                maintenance_ids = staff_lib.search_value("../Data/maintenances.txt", 3, type, 0)

                if maintenance_ids == False:
                    print(f"{color.RED}No record.{color.RESET}\n")
                    continue
                
                maintenances, header = staff_lib.read_csv_file("../Data/maintenances.txt")

                print("-" * 125)
                for column in header:
                    print(f"{color.BOLD}{column.replace('_', ' ').upper():<15}{color.RESET}", end='')
                print()
                print("-" * 125)

                # Iterate throught the list of all maintenances
                for maintenance in maintenances:
                    # Print the specific type only
                    if maintenance["type"] == type:
                        print(f"".join(staff_lib.format_csv_value(str(f"{value:<15}")) for value in maintenance.values()))
                        print("-" * 125)
                print()

            # Filter by status
            elif choice == 2:
                status = get_main_status()
                if status == 0:
                    return
                
                # Get the maintenance IDs of the specific status
                maintenance_ids = staff_lib.search_value("../Data/maintenances.txt", 5, status, 0)

                if maintenance_ids == False:
                    print(f"{color.RED}No record.{color.RESET}\n")
                    continue
                
                maintenances, header = staff_lib.read_csv_file("../Data/maintenances.txt")

                print("-" * 125)
                for column in header:
                    print(f"{color.BOLD}{column.replace('_', ' ').upper():<15}{color.RESET}", end='')
                print()
                print("-" * 125)

                # Iterate throught the list of all maintenances
                for maintenance in maintenances:
                    # Print the specific status only
                    if maintenance["status"] == status:
                        print(f"".join(staff_lib.format_csv_value(str(f"{value:<15}")) for value in maintenance.values()))
                        print("-" * 125)
                print()

        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
        return
