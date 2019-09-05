# Dependencies 
import os
import csv

# Import file.
csvpath = os.path.join(".", "", "employee_data.csv")

# Dictionary for Abrevs for each US state
states_dict = {
        'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona',
        'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 
        'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa',
        'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
        'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota',
        'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana',
        'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire',
        'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio',
        'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island',
        'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
        'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin',
        'WV': 'West Virginia', 'WY': 'Wyoming'
}

# New Header: Emp ID, First Name, Last Name, DOB, SSN, State
new_header = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
name_list = []
split_dates = []
ssn_list = []
new_employee_list = []

# Open file
with open(csvpath, newline='') as employee:
    reader = csv.reader(employee, delimiter=',')
    csv_header = next(reader)
    
    for emp_id,name,dob,ssn,state in reader:
        # Split the name in 2
        name_list = name.split(" ")
        first_name = name_list[0]
        last_name = name_list[1]
        
        # Convert DOB to DD/MM/YY
        split_dates = dob.split('-')
        dob = f'{split_dates[2]}/{split_dates[1]}/{split_dates[0]}'
        
        # Rewrite SSN to hide first 5 numbers.
        ssn_list = ssn.split('-')
        ssn = f'***-***-{ssn_list[2]}'
        
        # Change State Name to the Abv.
        for abv, state_name in states_dict.items():
            if state_name == state:
                state = abv
        
        list_element = [emp_id,first_name,last_name,dob,ssn,state]
        new_employee_list.append(list_element)


# Specify the file to write to
output_path = os.path.join(".", "", "new_employee_data.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(new_header)

    # Write the second row
    for row in range(len(new_employee_list)):
        csvwriter.writerow(new_employee_list[row])
