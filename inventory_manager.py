import json # to use json.dump() and json.load()
from abc import ABC, abstractmethod


# ---------------- Product classes ----------------

class Product(ABC):  # abstract class: cannot be instantiated directly
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_stock(self):
        return self._stock

    def update_stock(self, new_stock):
        self._stock = new_stock

    def display_information(self):
        print(f"ID: {self._product_id} | Name: {self._name} | Price: {self._price} | Stock: {self._stock}")

    def to_dict(self):
        return {"Name": self._name, "Price": self._price, "Stock": self._stock}

    @abstractmethod
    def get_fulfilment_info(self):
        pass


class CanBeShipped(ABC):  # interface-style abstract base class
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


class PhysicalProduct(Product, CanBeShipped):  # inherits Product, implements CanBeShipped
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight = float(weight)  # kilograms

    def display_information(self):
        super().display_information()  # reuse parent output
        print(f"    Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return round(self._weight * 2.0, 2)  # $2.00 per kg

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "physical"
        data["Weight"] = self._weight
        return data


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = float(download_size)  # megabytes

    def display_information(self):
        super().display_information()  # reuse parent output
        print(f"    Download Size: {self._download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "digital"
        data["Download Size"] = self._download_size
        return data


# ---------------- Inventory class ----------------

class Inventory:
    def __init__(self, filename="inventory.json"):
        self._filename = filename
        self._products = {}

    def add_product(self, product):
        self._products[product.get_product_id()] = product

    def get_product(self, product_id):
        return self._products.get(product_id)

    def update_stock(self, product_id, new_stock):
        self._products[product_id].update_stock(new_stock)

    def display_all_products(self):
        for product in self._products.values():
            product.display_information()

    def save(self):
        data = {product_id: product.to_dict() for product_id, product in self._products.items()}
        with open(self._filename, "w") as file:
            json.dump(data, file)

    def load(self):
        try:
            with open(self._filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return False
        for product_id, details in data.items():
            # use the type identifier to create the correct subclass
            if details["Type"] == "physical":
                product = PhysicalProduct(product_id, details["Name"], details["Price"],
                                          details["Stock"], details["Weight"])
            elif details["Type"] == "digital":
                product = DigitalProduct(product_id, details["Name"], details["Price"],
                                         details["Stock"], details["Download Size"])
            else:
                continue
            self.add_product(product)
        return True


# ---------------- Menu / user interaction ----------------

def show_menu():
    print("""
=======================================
INVENTORY MANAGEMENT SYSTEM
=======================================
""")
    inventory = Inventory()
    if inventory.load():
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
    inventory.display_all_products()
    print("=" * 30)

def add_product(inventory):
    print("Add New Product")
    product_type = input("Product Type (1. Physical / 2. Digital): ")
    if product_type not in ("1", "2"):
        print("Invalid product type")
        return
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = input("Price: ")
    stock_quantity = input("Stock Quantity: ")
    if product_type == "1":
        weight = input("Weight (kg): ")
        product = PhysicalProduct(product_id, product_name, price, stock_quantity, weight)
    else:
        download_size = input("Download Size (MB): ")
        product = DigitalProduct(product_id, product_name, price, stock_quantity, download_size)
    inventory.add_product(product)
    print("\n")
    print("Product added successfully!")

def update_stock(inventory):
    print("Update Stock")
    id = input("Enter Product ID: ")
    product = inventory.get_product(id)
    if product is not None:
        print("")
        print("Product Found:")
        print(f"Name: {product.get_name()}")
        print(f"Current Stock: {product.get_stock()}")
        print("")
        new_stock = input("New Stock Quantity: ")
        inventory.update_stock(id, new_stock)
    else:
        print("Choose another product id, invalid id")

def search_product(inventory):
    print("Search Product")
    id = input("Enter Product ID: ")
    product = inventory.get_product(id)
    if product is not None:
        print("")
        print("Product Found")
        print("=" * 30)
        product.display_information()
        print(f"Fulfilment: {product.get_fulfilment_info()}")
        if isinstance(product, CanBeShipped):  # only products that can be shipped
            print(f"Shipping Cost: ${product.calculate_shipping_cost()}")
        print("=" * 30)
    else:
        print("")
        print("Product not found.")

def save_inventory(inventory):
    print("Saving inventory...")
    inventory.save()
    print("Inventory saved successfully to inventory.json")


if __name__ == "__main__":
    inventory = show_menu()
    choose_option(inventory)
