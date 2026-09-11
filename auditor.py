inventory = 0
rejected_entries = 0

while (input !="quit"):
    stock = input("Enter stock quantity").lower()
    if stock.isdigit():
        if stock < 0:
            print("Stock cannot be negative")
            rejected_entires +=1
        else:
            stock = int(stock)
            inventory = inventory + stock
    else:
        print("Error")
        rejected_entires +=1

    if inventory > 500:
        print("Alert")
        break
    else:
        continue

print("Total Units Processed: " + inventory)
print("Number of Failed/Rejected Entries " + rejected_entires)