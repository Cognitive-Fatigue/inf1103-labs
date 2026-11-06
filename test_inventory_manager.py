from inventory_manager import Product, PhysicalProduct, DigitalProduct, Inventory

# 1.2 / 1.3 / 2.2 - create products and display their information
guitar = PhysicalProduct("P001", "Guitar", 299.99, 10, 3.5)
os_license = DigitalProduct("D001", "Operating System", 129.99, 50, 4500)
guitar.display_information()
os_license.display_information()

# 3.2 - fulfilment info
print(guitar.get_fulfilment_info())
print(os_license.get_fulfilment_info())

# 3.3 - abstract Product cannot be instantiated
try:
    Product("X001", "Generic", 1.0, 1)
except TypeError as error:
    print("Cannot create Product:", error)

# 4.2 - shipping cost with different weights
for weight in (0.5, 3.5, 20):
    item = PhysicalProduct("T", "Test", 1, 1, weight)
    print(f"Shipping for {weight} kg: ${item.calculate_shipping_cost()}")

# 5 - JSON save/load preserves product types
inventory = Inventory("test_inventory.json")
inventory.add_product(guitar)
inventory.add_product(os_license)
inventory.save()

reloaded = Inventory("test_inventory.json")
reloaded.load()
print(type(reloaded.get_product("P001")).__name__)
print(type(reloaded.get_product("D001")).__name__)
reloaded.display_all_products()
