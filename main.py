

class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability
        self.sales=0

# Create an empty inventory list
inventory = []
sales_records = []   # list to store sales record


def print_menu():
    print("Welcome to Delhi Munchies: The Canteen Chronicle")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update the availability of a snack")
    print("4. Sell a snack")
    print("5. See your Inventory")
    print("6. Exit")




def sell_snack(snack_id):
    try:
        snack_id = int(snack_id)
    except ValueError:
        print("Invalid snack ID. Please enter a valid number.")
        return

    for snack in inventory:
        if snack.snack_id == snack_id:
            if snack.availability == "yes":
                # Snack is available, update inventory and sales record
                snack.availability = "no"
                snack.sales += 1
                sales_records.append(snack)  # Add the sold snack to sales records
                print("Snack sold successfully.")
            else:
                print("Sorry, the snack is currently unavailable.")
            return

    print("Snack not found in the inventory.")





# Code to add a new snack to the inventory

def add_snack():
    snack_id = input("Enter snack ID: ")
    name = input("Enter snack name: ")

    # Validate price input
    while True:
        price = input("Enter snack price: ")
        try:
            price = float(price)
            break
        except ValueError:
            print("Invalid price. Please enter a valid number.")

    availability = input("Enter snack availability (yes/no): ")

    # Check if snack_id is already used
    for snack in inventory:
        if snack.snack_id == snack_id:
            print("Snack ID is already used. Please enter a unique ID.")
            return

    snack = Snack(snack_id, name, price, availability)
    inventory.append(snack)
    print("Snack added to the inventory.")

   

  # Code to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter the snack ID to remove: ")

    for snack in inventory:
        if snack.snack_id == snack_id:
            inventory.remove(snack)
            print("Snack removed from the inventory.")
            return

    print("Snack not found in the inventory.")

  
 # Code to update the availability of a snack 
def update_availability():
    snack_id = input("Enter the snack ID to update availability: ")

    for snack in inventory:
        if snack.snack_id == snack_id:
            new_availability = input("Enter new availability (yes/no): ")
            snack.availability = new_availability
            print("Availability updated.")
            return

    print("Snack not found in the inventory.")

    


def display_inventory():
    print("Snack Inventory:")
    for snack in inventory:
        print(f"ID: {snack.snack_id}")
        print(f"Name: {snack.name}")
        print(f"Price: {snack.price}")
        print(f"Availability: {snack.availability}")
        print("------------------")



while True:
    print_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        snack_id = input("Enter the snack ID to sell: ")
        sell_snack(snack_id)
    elif choice == "5":
        display_inventory()
   
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
