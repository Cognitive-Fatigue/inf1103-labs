inventory = 0
stock = ""

while (stock !="quit"):
    stock = input("Enter stock quantity: ").lower()
    if stock.isdigit():
        stock = int(stock)
    elif stock == "quit":
        break
    else:
        print("Error")


