# Dependencies
import os
import csv

budget_data = os.path.join(".", "Resources", "budget_data.csv")

# Initialize values for correct calculations.
greatest_increase = 0
greatest_decrease = 9999999999
net_change = 0

with open(budget_data, "r") as data:
    # Read file and skip header.
    reader = csv.reader(data)    
    data_header = next(reader)

    # Get data from first row.
    first_data = next(reader)
    total_months = 1
    total_net = int(first_data[1])
    prev_net = int(first_data[1])    

    for row in reader:

        # Update values.
        total_months += 1
        total_net += int(row[1])
        curr_change = int(row[1]) - prev_net
        net_change += curr_change
        prev_net = int(row[1])

        # Get greatest increase
        if curr_change > greatest_increase:
            great_inc_month = row[0]
            greatest_increase = curr_change
        
        # Get greatest decrease
        if curr_change < greatest_decrease:
            great_dec_month = row[0]
            greatest_decrease = curr_change

# Calcular avg change net.
avg_change = net_change / (total_months - 1)

print(f'''
        Total Months : {total_months}
        Total: ${total_net}
        Avg Change: ${round(avg_change,2)}
        Greatest Increase: {great_inc_month} (${greatest_increase})
        Greatest Decrease: {great_dec_month} (${greatest_decrease})
''')