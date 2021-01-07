# Import the os module
# This will allow me to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# List used to store the monthy results
monthly_result_list = []
# List used to store the monthy changes
change_list = []

# Reading using CSV module
with open(csvpath, encoding="utf8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents  = ['Date','Profit/Losses']
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    monthly_result_list = list(csvreader)
    # Get the number of months
    months = len(monthly_result_list)
    # Zip the original list in order to transpose values and manipulate Monthly Result (Profit/Loss) rows
    zipped_result_list = zip(*monthly_result_list)
    # Convert to list
    net_values_list = list(zipped_result_list)[1]
    # Cast values to float
    net_values_list_float = [float(value) for value in net_values_list]
    # Get rid of decimals since it contains integer value
    net_value = "{:.0f}".format(sum(net_values_list_float))
    # Create new list with monthly changes
    for counter in range(months):
        if counter==0:
        # First month has no changes
            change_list.append(0)
        else:
        # For following months change = current - previous
            change_list.append(net_values_list_float[counter]-net_values_list_float[counter-1])
    if len(change_list)>1:
    # If at leat 1 change
        average_change = "{:,.2f}".format(sum(change for change in change_list if change_list.index(change)>0)/(len(change_list)-1))
    else:
    # If no changes at all
        average_change = 0
    # Zip the original list in order to transpose values and manipulate date rows
    zipped_result_list = zip(*monthly_result_list)
    # Convert to list
    dates_list = list(zipped_result_list)[0]
    # Greatest increase is the maximum change in change list
    greatest_increase = max(change_list)
    # Get the corresponding date according to the index that the Greatest increase has 
    month_greatest_increase = dates_list[change_list.index(greatest_increase)] 
    # Get rid of decimals since it contains integer value
    greatest_increase = "{:.0f}".format(greatest_increase)
    # Greatest decrease is the minimum change in change list
    greatest_decrease = min(change_list)
    # Get the corresponding date according to the index that the Greatest decrease has 
    month_greatest_decrease = dates_list[change_list.index(greatest_decrease)] 
    # Get rid of decimals since it contains integer value
    greatest_decrease = "{:.0f}".format(greatest_decrease)

# Print the analysis to the terminal
print ("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months}')
print(f'Total: ${net_value}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})')

# Export the analysis to a text file with the results
# Save the output file path
output_file = os.path.join('.', 'analysis', 'output.txt')
# Open the output file and then write the  object to the txt
with open(output_file, "w", newline='') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Months: {months}\n')
    datafile.write(f'Total: {net_value}\n')
    datafile.write(f'Average Change: ${average_change}\n')
    datafile.write(f'Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})\n')
    datafile.write(f'Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})')