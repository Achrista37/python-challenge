# Path to collect data from local folder
import os
import csv
from typing import Text
budget_data_raw = os.path.join("Resources", "budget_data.csv")

# Assign values to variables
months = []
PnL=[]
data_pylist=[]
PnL_change = []
max_dec = 0
max_date = ""
min_date= ""
max_inc = 0

# Open CSV File, setting coma as delimiter 
with open(budget_data_raw) as csv_files:
    csv_reader = csv.reader(csv_files, delimiter=",")
    csv_header = next(csv_files)
    for row in csv_reader:
        months.append(row[0]) #adding values in to the list called "months"
        PnL.append(float(row[1])) #adding values in to the PnL list
#start printing desired text into the Terminal
print("Financial Analysis")
print("-----------------------------------------")
#calculate & print total months in the csv report
print("Total Months:" + str(len(months)))
#calculate total in PnL in the csv report
print("Total: $" + str(sum(PnL)))

#start working towards calculating the average change in P&L
#write a code that will substract the PnL value wihtin a particular month from the previous one
#for that the loop calculation has to start with the second month, and skip substraction starting from the first month
#skip first month
skipped_first_line = False
for row in PnL:
    if (skipped_first_line == False):
        skipped_first_line = True
        current_value = row
        pass
    else:
        previous_value = current_value
        current_value = row
        PnL_change.append(current_value - previous_value)
#print into the Terminal the Average Change in P&L
print("Average Change in Profit/Losses: $ "+ (str(round(sum(PnL_change)/len(months)))))
#start building a new list that will contain months and the average change in P&L as a base for the next calculations
#the new list will be a result of zipping a new list of month_newlist (with the first month from the previous list taken out) and the average change in P&L value
#eliminating the first month from the original list
months_newlist = months[1:]       
# Zip lists together
PnL_zip = zip(months_newlist, PnL_change)
#loop through PnL_zip to find max increase in profit, with its paired month value and max decrease in profit, with its paired month value
for date, profit in PnL_zip:
    if max_inc<profit:
        max_inc = profit
        max_date = date
    if max_dec>profit:
        max_dec = profit
        min_date = date
print(f"Greatest Increase in Profits:  {max_date} ($ {max_inc}) ")
print(f"Greatest Decrease in Profits:  {min_date} ($ {max_dec}) ")


# Set variable for output file
output_file = os.path.join("Analysis", "pyBank.txt")


#output_file = os.path.join("pyBank.txt")
#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------------------------------\n")
    text_file.write("Total Months: "+ str(len(months)) + "\n")
    text_file.write("Total: $ "+ str(sum(PnL))+  "\n")
    text_file.write("Average Change in Profit/Losses: $" + (str(sum(PnL)/len(months)))+ "\n")
    text_file.write("Greatest increase in profits: " + max_date+ str(max_inc)+ ")\n")
    text_file.write("Greatest decrease in losses: "+ min_date + str(max_dec)+ ")\n")
