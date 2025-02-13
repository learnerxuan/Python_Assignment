def choose(choice):
    while True:
        try:
            num = int(input(f"Enter number ({choice[0]}-{choice[-1]}): "))
            if num in choice:
                return num
            else:
                print(f"Please enter a number between {choice[0]} and {choice[-1]}.")
        except ValueError:
            print(f"Invalid input. Please enter a number between {choice[0]} and {choice[-1]}.")
