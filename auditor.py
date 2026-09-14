inventory = 0
stock = ""

while (stock !="quit"):
    stock = input("Enter stock quantity: ").lower()
    if stock.isdigit():   # only accepts digits, does not recognise "-" sign
        stock = int(stock)
        inventory += stock
    elif stock == "quit":
        break
    elif "-" in stock:
        print("No negative numbers")
    else:
        print("Error")

print(inventory)

