def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            print("Invalid input. Please enter a Valid Number")

def get_valid_name(prompt):
    while True:
        name = input (prompt)
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid. Please enter a Valid Name")