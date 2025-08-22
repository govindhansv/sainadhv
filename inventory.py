inventory = {
    "apple": {"quantity": 10, "price": 30},
    "banana": {"quantity": 20, "price": 10},
    "mango": {"quantity": 15, "price": 50}
}

while True:
    print("\nEnter choice : 1.Add 2.Remove 3.Display 4.Exit")
    ch = input("Enter your choice: ")

    if ch == "1":  # Add item
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        
        if name in inventory:
            inventory[name]["quantity"] += qty
            inventory[name]["price"] = price   # update price if changed
            print("Item updated successfully")
        else:
            inventory[name] = {"quantity": qty, "price": price}
            print("Item added successfully")

    elif ch == "2":  # Remove item
        name = input("Enter item name to remove: ")
        if name in inventory:
            del inventory[name]
            print(f"{name} removed successfully")
        else:
            print("Item not found in inventory")

    elif ch == "3":  # Display items
        print("\nInventory:")
        for name, details in inventory.items():
            print(f"{name} - Quantity: {details['quantity']}, Price: {details['price']}")

    elif ch == "5":  # Exit
        print("Applying Discount... \n")
        discount = int(input("Enter discount % :"))
        for name,details in inventory.items():
            details['price'] =  details['price']*(100-discount)/100
            
    elif ch == "4":  # Exit
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
