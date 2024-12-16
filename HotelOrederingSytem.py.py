print("Welcome to My Taj ")  # Welcome message

# Variables to track orders and total bill
order = []
total_bill = 0

def display_summary():
    """Display the order summary and total bill."""
    print("\nYour Order Summary:")
    for item in order:
        print(f"- {item}")
    print(f"Total Bill: {total_bill} Rs")
    print("Thank you for visiting! Goodbye.")

def validate_input(prompt, valid_options):
    """Get validated input from the user."""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_options:
                return user_input
            else:
                print(f"Invalid choice. Please select one of {valid_options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

while True:
    # Display food type options
    print("\n1: Veg \n2: Non-veg")
    food_type = validate_input("Select your food type: ", [1, 2])

    # Display dining options
    print("\n1: Dine \n2: Take-Away")
    dining_choice = validate_input("Select your dining option: ", [1, 2])

    while True:  # Nested loop for menu
        # Display menu categories
        print("\n1: Starters\n2: Main Course\n3: Desserts\n4: Drinks\n5: Finalize Order")
        menu_choice = validate_input("Select what you want to order: ", [1, 2, 3, 4, 5])

        # Handling different menu choices
        if menu_choice == 1:  # Starters menu
            print("\nStarters Menu:")
            print("1: Item1 - 250 Rs")
            print("2: Item2 - 200 Rs")
            st = validate_input("Select your food: ", [1, 2])
            if st == 1:
                order.append("Starter Item1")
                total_bill += 250
            elif st == 2:
                order.append("Starter Item2")
                total_bill += 200

        elif menu_choice == 2:  # Main Course menu
            print("\nMain Course Menu:")
            print("1: Item1 - 500 Rs")
            print("2: Item2 - 450 Rs")
            mc = validate_input("Select your food: ", [1, 2])
            if mc == 1:
                order.append("Main Course Item1")
                total_bill += 500
            elif mc == 2:
                order.append("Main Course Item2")
                total_bill += 450

        elif menu_choice == 3:  # Desserts menu
            print("\nDesserts Menu:")
            print("1: Item1 - 150 Rs")
            print("2: Item2 - 120 Rs")
            ds = validate_input("Select your food: ", [1, 2])
            if ds == 1:
                order.append("Dessert Item1")
                total_bill += 150
            elif ds == 2:
                order.append("Dessert Item2")
                total_bill += 120

        elif menu_choice == 4:  # Drinks menu
            print("\nDrinks Menu:")
            print("1: Item1 - 100 Rs")
            print("2: Item2 - 80 Rs")
            dr = validate_input("Select your food: ", [1, 2])
            if dr == 1:
                order.append("Drink Item1")
                total_bill += 100
            elif dr == 2:
                order.append("Drink Item2")
                total_bill += 80

        elif menu_choice == 5:  # Finalize order
            print("\nFinalizing your order...")
            display_summary()
            exit()  # Exit the program

        # Ask if the user wants to add more items
        add_more = input("\nDo you want to add more items? (yes/no): ").strip().lower()
        if add_more == "no":
            print("\nFinalizing your order...")
            display_summary()
            exit()  # Exit the program
