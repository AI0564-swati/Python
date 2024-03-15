import json

# To create, open and load file
def create_file():
    try:
        with open("file.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# To save list into file
def save_list(inventory):
    with open("file.json", "w") as file:
        json.dump(inventory, file, indent=4)

# To add new item to the file
def add_item(inventory):
    name = input("Item Name: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = quantity
    save_list(inventory)
    print("Successfully added")

# To update quantity 
def update_quantity(inventory):
    name = input("Item Name: ")
    if name in inventory:
        quantity = int(input("New quantity: "))
        inventory[name] = quantity
        save_list(inventory)
        print("Successfully updated")
    else:
        print("Invalid item")

# To remove item
def remove_item(inventory):
    name = input("Item name: ")
    if name in inventory:
        del inventory[name]
        save_list(inventory)
        print("Successfully removed")
    else:
        print("Invalid item")

# To read file and display
def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(item + ": " + str(quantity))
    print()

# Operations
def main():
    inventory = create_file()
    while True:
        print("\nMenu:")
        print("a. Add new item to the inventory")
        print("b. Update quantity of an existing item")
        print("c. Remove an item from the inventory")
        print("d. Display the current inventory")
        print("e. Exit the program")
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            add_item(inventory)
        elif choice == 'b':
            update_quantity(inventory)
        elif choice == 'c':
            remove_item(inventory)
        elif choice == 'd':
            display_inventory(inventory)
        elif choice == 'e':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
