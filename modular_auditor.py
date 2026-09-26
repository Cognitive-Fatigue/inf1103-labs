

def get_valid_input():
        stock = input("Enter stock quantity: ").lower()
        if stock.isdigit():
            return stock   # only accepts digits, does not recognise "-" sign
        elif stock == "quit":
              return "quit"
        else:
              return "invalid"

def process_delivery(current_total, new_value):
    if new_value.isdigit():
        new_value = int(new_value)
        current_total += new_value
        current_total += calculate_tax(new_value)
        return current_total

def calculate_tax(amount):
    amount = amount * 0.1
    return amount

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed: " + str(total_units))
    print("Number of Failed/Rejected Entries: " + str(failed_attempts))


stock = ""
inventory = 0
rejected_entries = 0

while stock !="quit":
    stock = get_valid_input()
    if stock.isdigit():
        inventory = process_delivery(inventory,stock) 
    elif stock == "invalid":
        rejected_entries +=1
    else:
        break

generate_report(inventory,rejected_entries)
