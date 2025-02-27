import staff_lib

event_domains = {1: "Academic", 2: "Extracurricular"}
event_types = {1: "Conference", 2:"Seminar"}


def events():
    """Display resource management menu and processes user choices."""
    while True:
        print("""
1. Create New Event
2. Edit Event
3. Delete Event
4. View All Events
5. Filter Events
6. Search Events
0. Back""")
        
        # Get user input and validate it
        choice = staff_lib.choose([0, 1, 2, 3, 4, 5, 6])

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
        elif choice == 6:
            search_event()
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