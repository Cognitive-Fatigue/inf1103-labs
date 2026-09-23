inventory = 0
stock = ""
rejected_entries = 0

while (stock !="quit"):
    stock = input("Enter stock quantity: ").lower()
    if stock.isdigit():   # only accepts digits, does not recognise "-" sign
        stock = int(stock)
        inventory += stock
        if inventory > 500:
                print("Alert")
                break
    elif stock == "quit":
        break
    elif "-" in stock:
        print("No negative numbers")
        rejected_entries += 1
    else:
        print("Error")
        rejected_entries += 1

print("Total Units Processed: " + str(inventory))
print("Number of Failed/Rejected Entries: " + str(rejected_entries))

