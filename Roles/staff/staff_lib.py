def choose(choice):
    """Validates user choice and returns a number from the given list of choices passed as an argument."""
    while True:
        try:
            num = int(input(f"Enter number ({choice[0]}-{choice[-1]}): ").strip())
            if num in choice:
                return num
            else:
                print(f"Please enter a number between {choice[0]} and {choice[-1]}.")
        except ValueError:
            print(f"Invalid input. Please enter a number between {choice[0]} and {choice[-1]}.")


def format_csv_value(value):
    """Returns the value wrapped in quotes if it contains a comma."""
    return f'"{value}"' if ',' in value else value


def read_csv_line(line):
    """Parses a CSV line into a list of fields, handling quoted values correctly."""
    fields = []
    field = ''
    inside_quotes = False

    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes  # Toggle inside_quotes
        elif char == ',' and not inside_quotes:
            fields.append(field)
            field = ''
        else:
            field += char

    fields.append(field)  # Append last field
    return fields
    

def search_value(file_path, column_index, search_value, return_column=None):
    """
    Checks if the given search_value exists in the specified column of the file.
    return_column returns the value of the specified column of the same row that the search value was found.
    If return_column is not specified
        - Returns True if at least found one
        - Returns Flase if not found
    If return_column is specified
        - Returns the value if only exist one 
        - Returns a list of value if multiple match
        - Returns False if not found
    """
    results = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                columns = read_csv_line(line.strip())
                if column_index < len(columns) and columns[column_index] == search_value:
                    if return_column is not None and return_column < len(columns):
                        results.append(columns[return_column])
                    else:
                        return True
                
        # Handling different result cases
        if not results:
            return False
        elif len(results) == 1:
            return results[0]  # Return single value if only one match
        return results  # Return list if multiple matches found
    
    except Exception:
        return False


def read_csv_file(file_path):
    """
    Reads a CSV file and stores each record as a dictionary, using the header as keys, stored in a list.
    Returns the list and header
    """

    # List to temporarily store all record
    list_name = []

    with open(file_path, "r") as file:
        header = file.readline().strip().split(",")
        for line in file:
            try:
                # Pass the line (record) into staff_lib.read_csv_line and assign the return value (a list) into a variable
                fields = read_csv_line(line.strip())

                # Skip the line if the line does not have the same number of column as header
                if len(fields) != len(header):
                    continue

                # Append each record as a dictionary
                list_name.append(dict(zip(header, fields)))
                
            except ValueError:
                continue
    return list_name, header


def new_id(last_id, prefix_length):
    """
    Generates the next ID by extracting the numeric part, incrementing it, and formatting it with leading zeros.
    Returns the next_id
    """
    prefix, number = last_id[:prefix_length], last_id[prefix_length:]
    next_number = int(number) + 1
    next_id = f"{prefix}{next_number:0{len(number)}}"
    return next_id

