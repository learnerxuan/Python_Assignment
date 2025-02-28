import staff_lib

event_domains = {1: "Academic", 2: "Extracurricular"}
event_types = {1: "Conference", 2:"Seminar"}


def events():
    """Display event menu and processes user choices."""
    while True:
        print("""
1. Create New Event
2. Edit Event
3. Delete Event
4. View All Events
5. Filter Events
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5])

        if choice == 1:
            new_event()
        elif choice == 2:
            edit_event()
        elif choice == 3:
            delete_event()
        elif choice == 4:
            all_event()
        elif choice == 5:
            filter_event()
        elif choice == 0:
            # Return back to staff menu
            return
    

def get_event_domain():
    """Returns event domain in string."""
    print("Select Event Domain:")
    for key, value in event_domains.items():
        print(f"{key} - {value}")
    while True:
        try:
            domain_num = int(input("Enter event domain (1 or 2) (0 to cancel): ").strip())
            if domain_num == 0:
                return 0

            if domain_num in event_domains:
                domain = event_domains[domain_num]
                return domain
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")
            continue


def get_event_type():
    """Returns event type in string."""
    print("Select Event Type:")
    for key, value in event_types.items():
        print(f"{key} - {value}")
    while True:
        try:
            type_num = int(input("Enter event type (1 or 2) (0 to cancel): ").strip())
            if type_num == 0:
                return 0

            if type_num in event_types:
                type = event_types[type_num]
                return type
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")
            continue


def new_event():
    """Create new event"""
    try:
        # Get event name
        event_name = input("Enter event name (0 to cancel): ").strip()
        if event_name == "0":
            return
        
        # Get event domain
        event_domain = get_event_domain()
        if event_domain == 0:
            return
        
        # Get event type
        event_type = get_event_type()
        if event_type == 0:
            return
        
        # Get event date
        date = staff_lib.get_date()
        if date == "0":
            return
        
        # Get start time
        print("Start Time")
        start_time = staff_lib.get_time()
        if start_time == "0":
            return

        # Get end time
        print("End Time")
        end_time = staff_lib.get_time()
        if end_time == "0":
            return

        # Get max attendees
        while True:
            try:
                max_attendees = int(input("Enter maximum attendees (0 to cancel): "))
                if max_attendees == 0:
                    return
                break
            except ValueError:
                print("Invalid input. Numbers only.")
                continue

        # Get location
        locations, header = staff_lib.read_csv_file("./Data/locations.txt")
        # Create a list to store locations that can fit max attendees
        locations_available = []
        print("Locations available according to maximum attendees:")
        print(",".join(header))
        # Display locations available
        for location in locations:
            if int(location["capacity"]) >= max_attendees:
                locations_available.append(location["location_name"])
                print(",".join(staff_lib.format_csv_value(location.values())))
        # Validate location's input
        while True:
            location = input("Enter location (0 to cancel): ").strip().title()
            if location == "0":
                return
            if location in locations_available:
                break
            print("Invalid location. Please try again.")

        # Generate new ID for the event
        events, _ = staff_lib.read_csv_file("./Data/events.txt")

        if events:  # Check if the list is not empty
            last_id = events[-1]["event_id"]
            next_id = staff_lib.new_id(last_id, 3)  # Increment ID
        else: 
            next_id = "EVT001"  # Default starting ID if no records exist

        # Add new record
        with open("./Data/events.txt", "a") as file:
            file.write(f"{next_id},{staff_lib.format_csv_value(event_name)},{event_domain},{event_type},{date},{start_time},{end_time},{max_attendees},{staff_lib.format_csv_value(location)}\n")
        print("Successfully added!") 

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")
    return


def edit_event():
    """Edit event details"""
    while True:
        try:
            # Input event ID user wants to edit
            event_id = input("Enter event ID (0 to cancel): ").strip()

            if event_id == "0":
                return

            # Check if event ID exist
            if not staff_lib.search_value("./Data/events.txt", 0, event_id):
                print("Invalid event ID")
                continue
            
            while True:
                print("""
1. Edit name
2. Edit domain
3. Edit type
4. Edit date
5. Edit start time
6. Edit end time
7. Edit maximum attendees
8. Edit location
0. Back""")
                choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6, 7, 8])

                if choice == 0:
                    return
                elif choice == 1:
                    field = "event_name"
                elif choice == 2:
                    field = "event_domain"
                elif choice == 3:
                    field = "event_type"
                elif choice == 4:
                    field = "date"
                elif choice == 5:
                    field = "start_time"
                elif choice == 6:
                    field = "end_time"
                elif choice == 7:
                    field = "max_attendees"
                elif choice == 8:
                    field = "location"

                events, header = staff_lib.read_csv_file("./Data/events.txt")

                for event in events:
                    if event["event_id"] == event_id:

                        if field == "event_name":
                            new_detail = input("Enter new event name (0 to cancel): ").strip().title()
                            if new_detail == "0":
                                break

                        elif field == "event_domain":
                            new_detail = get_event_domain()
                            if new_detail == 0:
                                break
                        
                        elif field == "event_type":
                            new_detail = get_event_type()
                            if new_detail == 0:
                                break

                        elif field == "date":
                            new_detail = staff_lib.get_date()       
                            if new_detail == "0":
                                break

                        elif field == "start_time":
                            print("Start Time")
                            new_detail = staff_lib.get_time()   
                            if new_detail == "0":
                                break
                            
                        elif field == "end_time":
                            print("End Time")
                            new_detail = staff_lib.get_time()
                            if new_detail == "0":
                                continue
                            
                        elif field == "max_attendees":
                            while True:
                                try:
                                    new_detail = int(input("Enter maximum attendees (0 to cancel): "))
                                    if new_detail == 0:
                                        break
                                    break
                                except ValueError:
                                    print("Invalid input. Numbers only.")
                                    continue       

                        elif field == "location":
                            # Get location
                            locations, Lheader = staff_lib.read_csv_file("./Data/locations.txt")
                            # Create a list to store locations that can fit max attendees
                            locations_available = []
                            print("Locations available according to maximum attendees:")
                            print(",".join(Lheader))
                            # Display locations available
                            for location in locations:
                                if int(location["capacity"]) >= int(event["max_attendees"]):
                                    locations_available.append(location["location_name"])
                                    print(",".join(staff_lib.format_csv_value(location.values())))
                            # Validate location's input
                            while True:
                                new_detail = input("Enter location (0 to cancel): ").strip().title()
                                if new_detail == "0":
                                    break
                                if new_detail in locations_available:
                                    break
                                print("Invalid location. Please try again.")
                            
                        event[field] = new_detail # Update event's field

                        # Write newly changed data to file
                        with open("./Data/events.txt", "w") as writer:
                            writer.write(",".join(header) + "\n")
                            for event in events:
                                # Only write the value of each key-value pair for each resource
                                writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in event.values()) + "\n")
                            print(f"{field.capitalize().replace("_", " ")} updated successfully.")
                            break                  

        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file")
        return


def delete_event():
    """User inputs event ID and event will be deleted"""
    while True:
        try:
            event_id = input("Enter event ID (0 to cancel): ").strip()

            if event_id == "0":
                return

            # Validate the presence of event ID
            if not staff_lib.search_value("./Data/events.txt", 0, event_id):
                print("Invalid event ID.")
                continue
            
            events, header = staff_lib.read_csv_file("./Data/events.txt")

            # Append the list with all the other event except the one user intends to delete
            events = [event for event in events if event["event_id"] != event_id]

            # Write newly changed data to file
            with open("./Data/events.txt", "w") as writer:
                writer.write(",".join(header) + "\n")
                for event in events:
                    # Only write the value of each key-value pair for each resource
                    writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in event.values()) + "\n")
                print(f"Event successfully deleted.")
                break

        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Unable to read/write the file")
    return


def all_event():
    """View all events"""
    try:
        events, header = staff_lib.read_csv_file("./Data/events.txt")
        # Print all events
        print(','.join(header))
        for event in events:
            print(','.join(event.values()))
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")


def filter_event():
    """View events by filtering with domains or types"""
    try:
        print("Filter event by:\n1 - Domain\n2 - Type")
        choice = staff_lib.choose([1, 2])

        if choice == 0:
            return
        
        elif choice == 1:
            # Set the key and values to search for in a list of dict
            key = "event_domain"
            value = get_event_domain()

        elif choice == 2:
            # Set the key and values to search for in a list of dict
            key = "event_type"
            value = get_event_type()

        # Get every events as a dict and appended into a list
        events, header = staff_lib.read_csv_file("./Data/events.txt")
        print(','.join(header))

        # Iterate though the list of dict and search for the events
        for event in events:
            if event[key] == value:
                print(','.join(event.values()))
                return
        
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Unable to read/write the file")
    return
