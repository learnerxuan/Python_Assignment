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
                print("Good, Used, Fair, Needs Repair")
                get_resource("condition", input("Enter resource condition: ").strip().upper())
    
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
