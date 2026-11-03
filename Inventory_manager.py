import json

class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        # Using double underscores for strong internal encapsulation / privacy convention
        self.__product_id = str(product_id)
        self.__name = str(name)
        self.__price = float(price)
        self.__stock_quantity = int(stock_quantity)

    # Getters to safely expose specific information read-only to outside classes
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock_quantity

    # Enforces Encapsulation: State modifications occur strictly inside the class
    def update_stock(self, quantity):
        self.__stock_quantity = int(quantity)

    # SRP: The product handles its own single record formatting
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: {self.__price:.2f} | Stock: {self.__stock_quantity}")

    # Helper method to serialize an object back into a dictionary for JSON output
    def to_dict(self):
        return {
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock_quantity
        }


class Inventory:
    def __init__(self):
        # Stores a dictionary mapping product_id (string) -> Product object instance
        self.__products = {}

    def add_product(self, product):
        self.__products[product.get_id()] = product

    def search_product(self, product_id):
        return self.__products.get(product_id, None)

    def get_all_products(self):
        return self.__products.values()

    def display_all(self):
        print("Current Inventory")
        print("=" * 45)
        if not self.__products:
            print("No products currently in inventory.")
        for product in self.__products.values():
            product.display_information()
        print("=" * 45)


# =====================================================================
# MAIN PROGRAM & FILE HANDLING RESPONSIBILITIES
# =====================================================================

def load_inventory():
    inventory_obj = Inventory()
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            print("inventory.json found.\nInventory loaded successfully.\n")
            for pid, details in data.items():
                # Reconstruct Product objects from the saved raw JSON dictionary data
                prod = Product(pid, details["Name"], details["Price"], details["Stock"])
                inventory_obj.add_product(prod)
    except FileNotFoundError:
        print("inventory.json not found.\nInventory created successfully.\n")
        # Save an empty JSON profile immediately to initialize the file
        with open("inventory.json", "w") as file:
            json.dump({}, file)
    return inventory_obj

def save_inventory(inventory):
    print("Saving inventory...")
    raw_data = {}
    for product in inventory.get_all_products():
        raw_data[product.get_id()] = product.to_dict()
        
    with open("inventory.json", "w") as file:
        json.dump(raw_data, file, indent=4)
    print("Inventory saved successfully to inventory.json")

def show_menu():
    print("""
=======================================
INVENTORY MANAGEMENT SYSTEM
=======================================
    -------MENU---------
    1. Display All Products
    2. Add Product
    3. Update Stock
    4. Search Product
    5. Save Inventory
    6. Exit
    ----------------------
    """)

def run_system():
    inventory = load_inventory()
    
    while True:
        show_menu()
        mode = input("Enter option: ").strip()
        print("\n")
        
        if mode == "1":
            inventory.display_all()
            
        elif mode == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            
            # Check if product ID already exists to prevent unintentional overwriting
            if inventory.search_product(product_id):
                print("Error: Product ID already exists!")
                continue
                
            product_name = input("Product Name: ")
            price = input("Price: ")
            stock_quantity = input("Stock Quantity: ")
            
            try:
                new_product = Product(product_id, product_name, price, stock_quantity)
                inventory.add_product(new_product)
                print("\nProduct added successfully!")
            except ValueError:
                print("Invalid input values for price or stock. Please try again.")

        elif mode == "3":
            print("Update Stock")
            pid = input("Enter Product ID: ")
            product = inventory.search_product(pid)
            if product:
                print(f"\nProduct Found:")
                print(f"Name: {product.get_name()}")
                print(f"Current Stock: {product.get_stock()}\n")
                new_stock = input("New Stock Quantity: ")
                product.update_stock(new_stock)
                print("Stock updated successfully.")
            else:
                print("Choose another product id, invalid id")

        elif mode == "4":
            print("Search Product")
            pid = input("Enter Product ID: ")
            product = inventory.search_product(pid)
            if product:
                print("\nProduct Found")
                print("=" * 45)
                product.display_information()
                print("=" * 45)
            else:
                print("\nProduct not found.")

        elif mode == "5":
            save_inventory(inventory)

        elif mode == "6":
            save_inventory(inventory)
            print("Saving inventory before exit...")
            print("Inventory saved successfully.")
            print("\nThank you for using the Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Pick again, invalid option")

if __name__ == "__main__":
    run_system()
