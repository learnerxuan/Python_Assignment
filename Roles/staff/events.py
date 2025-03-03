import staff_lib
import color

event_domains = {1: "Academic", 2: "Extracurricular"}
event_types = {1: "Conference", 2:"Seminar"}

def events():
    """Display event menu and process user choices."""
    while True:
        print(f"{'=' * 22}{color.BOLD}{color.BLUE} EVENTS {color.RESET}{'=' * 22}")
        print(f"""{" " * 15}{color.YELLOW}1.{color.RESET}  Create New Event
{" " * 15}{color.YELLOW}2.{color.RESET}  Edit Event
{" " * 15}{color.YELLOW}3.{color.RESET}  Delete Event
{" " * 15}{color.YELLOW}4.{color.RESET}  View All Events
{" " * 15}{color.YELLOW}5.{color.RESET}  Filter Events
{" " * 15}{color.YELLOW}0.{color.RESET}  Back""")
        print(f"{'=' * 52}")

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
    print(f"{color.YELLOW}Select Event Domain:{color.RESET}")
    for key, value in event_domains.items():
        print(f"{key} - {value}")
    while True:
        try:
            domain_num = int(input(f"{color.GREEN}Enter event domain (1 or 2) (0 to cancel): {color.RESET}").strip())
            print()
            if domain_num == 0:
                return 0

            if domain_num in event_domains:
                domain = event_domains[domain_num]
                return domain
            else:
                print(f"{color.RED}Invalid choice. Please enter 1 or 2.{color.RESET}\n")
        except ValueError:
            print(f"{color.RED}Invalid choice. Please enter 1 or 2.{color.RESET}\n")
            continue


def get_event_type():
    """Returns event type in string."""
    print(f"{color.YELLOW}Select Event Type:{color.RESET}")
    for key, value in event_types.items():
        print(f"{key} - {value}")
    while True:
        try:
            type_num = int(input(f"{color.GREEN}Enter event type (1 or 2) (0 to cancel): {color.RESET}").strip())
            print()
            if type_num == 0:
                return 0

            if type_num in event_types:
                type = event_types[type_num]
                return type
            else:
                print(f"{color.RED}Invalid choice. Please enter 1 or 2.{color.RESET}\n")
        except ValueError:
            print(f"{color.RED}Invalid choice. Please enter 1 or 2.{color.RESET}\n")
            continue


def new_event():
    """Create new event"""
    try:
        print(f"{'=' * 16}{color.BOLD}{color.BLUE} CREATE NEW EVENT {color.RESET}{'=' * 17}")
        # Get event name
        event_name = input(f"{color.GREEN}Enter event name (0 to cancel): {color.RESET}").strip()
        print()
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
                max_attendees = int(input(f"{color.GREEN}Enter maximum attendees (0 to cancel): {color.RESET}").strip())
                print()
                if max_attendees == 0:
                    return
                break
            except ValueError:
                print(f"{color.RED}Invalid input. Numbers only.{color.RESET}\n")
                continue

        # Get location
        locations, header = staff_lib.read_csv_file("./Data/locations.txt")
        # Create a list to store locations that can fit max attendees
        locations_available = []
        print(f"{color.YELLOW}Locations available according to maximum attendees:{color.RESET}")
        print("-" * 40)
        for column in header:
            print(f"{color.BOLD}{column.replace('_', ' ').upper():<20}{color.RESET}", end='')
        print()
        print("-" * 40)
        # Display locations available
        for location in locations:
            if int(location["capacity"]) >= max_attendees:
                locations_available.append(location["location_name"])
                print("".join(f"{value:<20}" for value in location.values()))
                print("-" * 40)
        # Validate location's input
        while True:
            location = input(f"{color.GREEN}Enter location (0 to cancel): {color.RESET}").strip().title()
            print()
            if location == "0":
                return
            if location in locations_available:
                break
            print(f"{color.RED}Invalid location. Please try again.{color.RESET}\n")

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
        print(f"{color.GREEN}Successfully added!{color.RESET}\n") 

    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    return


def edit_event():
    """Edit event details"""
    while True:
        try:
            print(f"{'=' * 20}{color.BOLD}{color.BLUE} EDIT EVENT {color.RESET}{'=' * 20}")
            # Input event ID user wants to edit
            event_id = input(F"{color.GREEN}Enter event ID (0 to cancel): {color.RESET}").strip()
            print()

            if event_id == "0":
                return

            # Check if event ID exist
            if not staff_lib.search_value("./Data/events.txt", 0, event_id):
                print(f"{color.RED}Invalid event ID.{color.RESET}\n")
                continue
            
            while True:
                print(f"""{" " * 15}{color.YELLOW}1.{color.RESET} Edit name
{" " * 15}{color.YELLOW}2.{color.RESET} Edit domain
{" " * 15}{color.YELLOW}3.{color.RESET} Edit type
{" " * 15}{color.YELLOW}4.{color.RESET} Edit date
{" " * 15}{color.YELLOW}5.{color.RESET} Edit start time
{" " * 15}{color.YELLOW}6.{color.RESET} Edit end time
{" " * 15}{color.YELLOW}7.{color.RESET} Edit maximum attendees
{" " * 15}{color.YELLOW}8.{color.RESET} Edit location
{" " * 15}{color.YELLOW}0.{color.RESET} Back""")
                print(f"{'=' * 52}")

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
                            new_detail = input(f"{color.GREEN}Enter new event name (0 to cancel): {color.RESET}").strip().title()
                            print()
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
                            print(f"{color.YELLOW}Start Time{color.RESET}")
                            new_detail = staff_lib.get_time()   
                            if new_detail == "0":
                                break
                            
                        elif field == "end_time":
                            print(f"{color.YELLOW}End Time{color.RESET}")
                            new_detail = staff_lib.get_time()
                            if new_detail == "0":
                                continue
                            
                        elif field == "max_attendees":
                            while True:
                                try:
                                    new_detail = int(input(f"{color.GREEN}Enter maximum attendees (0 to cancel): {color.RESET}").strip())
                                    print()
                                    if new_detail == 0:
                                        break
                                    break
                                except ValueError:
                                    print(f"{color.RED}Invalid input. Numbers only.{color.RESET}\n")
                                    continue       

                        elif field == "location":
                            # Get location
                            locations, Lheader = staff_lib.read_csv_file("./Data/locations.txt")
                            # Create a list to store locations that can fit max attendees
                            locations_available = []
                            print(f"{color.YELLOW}Locations available according to maximum attendees:{color.RESET}")
                            print("-" * 30)
                            for column in Lheader:
                                print(f"{color.BOLD}{column.replace('_', ' ').upper():<20}{color.RESET}", end='')
                            print()
                            print("-" * 30)
                            # Display locations available
                            for location in locations:
                                if int(location["capacity"]) >= int(event["max_attendees"]):
                                    locations_available.append(location["location_name"])
                                    print("".join(f"{value:<20}" for value in location.values()))
                                    print("-" * 30)
                            print()
                            # Validate location's input
                            while True:
                                new_detail = input(f"{color.GREEN}Enter location (0 to cancel): {color.RESET}").strip().title()
                                print()
                                if new_detail == "0":
                                    break
                                if new_detail in locations_available:
                                    break
                                print(f"{color.RED}Invalid location. Please try again.{color.RESET}\n")
                            
                        event[field] = new_detail # Update event's field

                        # Write newly changed data to file
                        with open("./Data/events.txt", "w") as writer:
                            writer.write(",".join(header) + "\n")
                            for event in events:
                                # Only write the value of each key-value pair for each resource
                                writer.write(",".join(staff_lib.format_csv_value(str(value)) for value in event.values()) + "\n")
                            print(f"{color.GREEN}{field.capitalize().replace("_", " ")} updated successfully.{color.RESET}\n")
                            break                  

        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
        return


def delete_event():
    """User inputs event ID and event will be deleted"""
    while True:
        try:
            print(f"{'=' * 19}{color.BOLD}{color.BLUE} DELETE EVENT {color.RESET}{'=' * 19}")
            event_id = input(f"{color.GREEN}Enter event ID (0 to cancel): {color.RESET}").strip()
            print()

            if event_id == "0":
                return

            # Validate the presence of event ID
            if not staff_lib.search_value("./Data/events.txt", 0, event_id):
                print(f"{color.RED}Invalid event ID.{color.RESET}\n")
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
                print(f"{color.GREEN}Event successfully deleted.{color.RESET}\n")
                break

        except FileNotFoundError:
            print(f"{color.RED}Error: File not found.{color.RESET}\n")
        except IOError:
            print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    return


def all_event():
    """View all events"""
    try:
        print(f"{'=' * 73}{color.BOLD}{color.BLUE} ALL EVENTS {color.RESET}{'=' * 73}")
        events, header = staff_lib.read_csv_file("./Data/events.txt")
        # Print all events
        print("-" * 159)
        for column in header:
            print(f"{color.BOLD}{column.replace('_', ' ').upper():<18}{color.RESET}", end='')
        print()
        print("-" * 159)
        for event in events:
            print("".join(f"{value:<18}" for value in event.values()))
            print("-" * 159)
        print()
    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")


def filter_event():
    """View events by filtering with domains or types"""
    try:
        print(f"{'=' * 73}{color.BOLD}{color.BLUE} FILTER EVENTS {color.RESET}{'=' * 73}")
        print(f"{color.YELLOW}Filter event by:{color.RESET}\n1 - Domain\n2 - Type")
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

        print("-" * 159)
        for column in header:
            print(f"{color.BOLD}{column.replace('_', ' ').upper():<18}{color.RESET}", end='')
        print()
        print("-" * 159)

        # Iterate though the list of dict and search for the events
        for event in events:
            if event[key] == value:
                print("".join(f"{value:<18}" for value in event.values()))
                print("-" * 159)
                return
        
    except FileNotFoundError:
        print(f"{color.RED}Error: File not found.{color.RESET}\n")
    except IOError:
        print(f"{color.RED}Error: Unable to read/write the file.{color.RESET}\n")
    return
