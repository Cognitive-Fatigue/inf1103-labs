inventory = 0
rejected_entries = 0
stock = ""

while (stock !="quit"):
    stock = input("Enter stock quantity: ").lower()
    if stock.isdigit():
        stock = int(stock)
        if stock < 0:
            print("No negative numbers")
            rejected_entries += 1
        else:
            inventory = inventory + stock
    else:
        print("Error")
        rejected_entries +=1

    if inventory > 500:
        print("Alert")
        break
    else:
        continue

print("Total Units Processed: " + str(inventory))
print("Number of Failed/Rejected Entries " + str(rejected_entries))