def choose(choice):
    """Validates user choice and returns a number from the given list of choices passed as an argument."""
    while True:
        try:
            num = int(input(f"Enter number ({choice[0]}-{choice[-1]}): "))
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