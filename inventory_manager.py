import json # to use json.dump() and json.load()

def show_menu():
    print("""
=======================================
INVENTORY MANAGEMENT SYSTEM
=======================================
""")
    inventory = load_inventory()
    if len(inventory) > 0:
        print("inventory.json found. \nInventory loaded succesfully.\n ")
    else:
        print("inventory.json not found. \nInventory created sucessfully.\n")
    print("""
    -------MENU---------
    1. Display All Products
    2. Add Product
    3. Update Stock
    4. Search Product
    5. Save Inventory
    6. Exit
    ----------------------

            """)
    return inventory


def load_inventory():
    try:
        with open("inventory.json","r+") as file:
            inventory = json.load(file)
        return inventory
    except FileNotFoundError:
        file = open("inventory.txt", "w+")
        return {}  # return an empty dictionary that will be recieved by current_inventory

def choose_option(inventory): 
    mode = 0
    while mode !="6":
        print("\n")
        mode = input("Enter option: ")
        print("\n")
        if mode == "1":
            display_all_products(inventory)
        elif mode == "2":
            add_product(inventory)
        elif mode == "3":
            update_stock(inventory)
        elif mode == "4":
            search_product(inventory)
        elif mode == "5":
            save_inventory(inventory)
        elif mode == "6":
            save_inventory(inventory)
            print("Saving inventory before exit...")
            print("Inventory saved successfully.")
            print("")
            print("Thank you for using the Inventory Management System.")
            print("Program terminated.")
        else: 
            print("Pick again, invalid option")

def display_all_products(inventory):
    print("Current Inventory")
    print("=" * 30)
    for id,details in inventory.items():
        print(f"""ID: {id} | Name: {details["Name"]} |
          Price: {details["Price"]} | Stock: {details["Stock"]}""")
    print("=" * 30)

def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = input("Price: ")
    stock_quantity = input("Stock Quantity: ")
    inventory[product_id] = {"Name":product_name, "Price":price, "Stock": stock_quantity}
    print("\n")
    print("Product added successfully!")
    return

def update_stock(inventory):
    print("Update Stock")
    id = input("Enter Product ID: ")
    if id in inventory:
        print("")
        print("Product Found:")
        print(f"Name: {inventory[id]["Name"]}") # access name in product id (dictionary)
        print(f"Current Stock: {inventory[id]["Stock"]}")  # access stock in product id (dictionary)
        print("")
        new_stock = input("New Stock Quantity: ")
        inventory[id]["Stock"] = new_stock   # assign new value to product id (dictionary)
    else:
        print("Choose another product id, invalid id")

def search_product(inventory):
    print("Search Product")
    id = input("Enter Product ID: ")
    if id in inventory:
        print("")
        print("Product Found")
        print("=" * 30)
        print(f"ID: {id}")
        print(f"Name: {inventory[id]["Name"]}")
        print(f"Price: {inventory[id]["Price"]}")
        print(f"Stock: {inventory[id]["Stock"]}") 
        print("=" * 30)
    else:
        print("")
        print("Product not found.")                

def save_inventory(inventory):
    print("Saving inventory...")
    with open("inventory.json","w") as file:
        json.dump(inventory,file)
    print("Inventory saved successfully to inventory.json")

inventory = {}
inventory = show_menu()
choose_option(inventory)
