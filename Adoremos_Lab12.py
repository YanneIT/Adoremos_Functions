def display_menu():
    """Displays the food menu with prices."""
    menu = {
        1: ("Adobo", 120.00),
        2: ("Sinigang", 150.00),
        3: ("Kare-Kare", 180.00),
        4: ("Lumpia", 100.00),
        5: ("Halo-Halo", 75.00),
    }
    print("\n--- Menu ---")
    for item, details in menu.items():
        print(f"{item}. {details[0]} - ₱{details[1]:.2f}")
    return menu

def get_order(menu):
    """Prompts the user to select an item from the menu."""
    while True:
        try:
            choice = int(input("\nEnter the number of the item you want to order: "))
            if choice in menu:
                item, price = menu[choice]
                print(f"You selected: {item} - ₱{price:.2f}")
                return price
            else:
                print("Invalid choice. Please choose a valid menu item.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(total_cost):
    """Handles payment processing, ensuring sufficient funds are provided."""
    while True:
        try:
            cash = float(input(f"\nTotal cost is ₱{total_cost:.2f}. Enter cash amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment accepted. Your change is ₱{change:.2f}. Thank you!")
                break
            else:
                print("Insufficient cash. Please provide enough money to cover the total cost.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    """Main function to simulate the food ordering system."""
    print("Welcome to the Filipino Food Ordering System!")
    menu = display_menu()
    total_cost = get_order(menu)
    process_payment(total_cost)

if __name__ == "__main__":
    main()
