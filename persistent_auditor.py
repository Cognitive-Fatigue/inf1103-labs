def get_valid_input():
    product = input("Enter Product Name: ")
    if product.lower().strip() == "quit":
        return "quit"
    quantity = input("Enter Quantity: ")
    if quantity.lower().strip() == "quit":
        return "quit"
    return product, quantity

def load_inventory():
    transaction_id = 1
    print("Current Orders: \n")
    with open("./inventory.txt", "r") as file:
        for i in file:
            print(f"{i}", end="")
            transaction_id += 1
    print("")
    return transaction_id

def save_inventory(order):
    with open("inventory.txt", "a") as file:
        file.write(order + "\n")

transaction_history = []

while True:
    transaction_id = load_inventory()
    transaction_id = transaction_id + 1000
    stock = get_valid_input()
    if stock =="quit":
        break
    product, quantity = stock
    stock = (f"{transaction_id}, {product}, {quantity}")
    print(f"\nNew Order Added: \n{stock}")
    transaction_history.append(stock)
    save_inventory(stock)
    print(f"\nOrder successfully saved to orders.txt\n")
