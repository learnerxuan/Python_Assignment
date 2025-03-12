def generate_new_id(file_path, prefix):
    """
    Generates a new ID by reading the last line from a file, extracting the numeric part,
    incrementing it, and formatting it with leading zeros.

    Parameters:
        file_path (str): Path to the file containing the IDs.
        prefix (str): The prefix for the ID (e.g., 'A', 'S', 'T', 'C', 'CLS', 'ASM').

    Returns:
        str: The next ID in sequence.
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        # If file is empty, return the first ID
        if not lines:
            return f"{prefix}001"

        # Get last non-empty line
        last_line = lines[-1].strip()
        while not last_line and lines:
            lines.pop()
            last_line = lines[-1].strip() if lines else None

        # If no valid last line, return the first ID
        if not last_line:
            return f"{prefix}001"

        # Extract the last ID
        last_id = last_line.split(",")[0]  # Get the first column (ID)

        # Extract numeric part manually
        number_part = ""
        for char in last_id:
            if char.isdigit():
                number_part += char

        next_number = int(number_part) + 1  # Increment the number
        new_id = f"{prefix}{str(next_number).zfill(len(number_part))}"  # Keep same length

        return new_id

    except FileNotFoundError:
        return f"{prefix}001"  # If file not found, start from 001