# Dependencies
import os
import csv

# Import file.
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Define auxiliary Lists
total_months = []
total_profit = []
monthly_change = []

# Open File
with open(csvpath, newline='') as budget:
    reader = csv.reader(budget, delimiter=',')
    csv_header = next(reader)
    
    total_net_amount = 0
    average_change = 0
    max_increase = 0
    max_decrease = 0    
    
    for row in reader:   
        # Get the total months in the data   .     
        total_months.append(row[0])            
        
        # Get the total amount of Profit/Loss.
        total_profit.append(int(row[1]))
        total_net_amount += int(row[1])    

    # Get average changes.
    for i in range(len(total_profit)-1):        
        monthly_change.append(total_profit[i+1]-total_profit[i])
        
    for i in range(len(monthly_change)):
        # Find the sum of monthly changes.
        average_change += monthly_change[i] 
        # Find Max Increase.
        if monthly_change[i] > max_increase:
            max_increase = monthly_change[i]
            # Get the month corresponding month for the max increase.
            max_increase_index = monthly_change.index(max_increase) + 1
        # Find Max Decrease.
        if monthly_change[i] < max_decrease:
            max_decrease = monthly_change[i]
            # Get the month corresponding month for the max decrease.
            max_decrease_index = monthly_change.index(max_decrease) + 1
    # Find the average change of the Data.
    average_change = average_change/len(monthly_change)
    
    # Print a Summary.
    print('')
    print ("Financial Analysis")    
    print ("------------------------------------")    
    print (f'Total Months: {len(total_months)}')
    print (f'Total Net: ${total_net_amount}')
    print (f'Average Changes: ${average_change}')  
    print (f'Greates Increase in Profit: ${max_increase} in {total_months[max_increase_index]}')
    print (f'Greates Decrease in Profit: ${max_decrease} in {total_months[max_decrease_index]}')    


# Define an Output path and a filename for that output.
output_file = os.path.join("..", "Outpath", "Analysis_Summary.txt")

with open(output_file,"w") as file:
    
    # Write methods to print to Financial Analysis.
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f'Total Net: ${total_net_amount}\n')
    file.write(f'Average Changes: ${average_change}\n')
    file.write(f"Greatest Increase in Profits: ${max_increase} in {total_months[max_increase_index]}\n")
    file.write(f"Greatest Decrease in Profits: ${max_decrease} in {total_months[max_decrease_index]}\n")
    