# Import modules
import os
import csv

#Set path and open the CSV file
data_raw = os.path.join("Resources", "election_data.csv")

# Assign values to variables
poll_details_dic= {}
name_candidate = {}
sorted_items= {}
percentage_calculation = 0
totalvote = 0
line_ = "------------------------------------\n"
print_election = ""

# Open CSV File, setting coma as the delimiter 
with open(data_raw) as csv_files:
    csv_dict_reader = csv.reader(csv_files, delimiter=",")
#get the header as to not interfere with the rest of the data
    csv_header = next(csv_files)

#add 1 to the totalvote variable for each row of the data
    for row in csv_dict_reader:
        totalvote +=1

#assign row number 2 from the CSV file into name_candidate
        name_candidate = row[2]
        if name_candidate not in poll_details_dic:
#for new candidate name encountered, add it to the poll_details_dic. If the name already existed, add 1 to the vote tally
            poll_details_dic[name_candidate] = 1
        else:
             poll_details_dic[name_candidate] += 1

#print all the data we have so far, per assignment instruction layout 
print("Election Results")
print(line_)
print("Total Votes:" + str(totalvote))
print(line_)


#get the percentages for each candidate from the paired value in the dictionary
for x in poll_details_dic:
    percentage_calculation = poll_details_dic[x]/totalvote*100 
    print_election += x + " : " + str(round(percentage_calculation)) + "%" + "(" + str(poll_details_dic[x]) + ")\n"
    
print(print_election)
print(line_)

#sort the poll_details_dic in descending order, based on the number of the votes, to yield the winner in the top row (row[0])
sorted_items = sorted(poll_details_dic.items() , reverse=True,  key=lambda x: x[1])

#print the winner a.k.a the top row (row[0])
print("Winner:" + str(sorted_items[0]))

#set path for the txt
output_file = os.path.join("Analysis", "PyPoll.txt")

#open txt and write Analysis Data
with open(output_file,"w") as file:
    file.write("Election Results\n")
    file.write(line_ + "\n")
    file.write("Total Votes:" + str(totalvote) + "\n")
    file.write(line_ + "\n")
    file.write(print_election + "\n")
    file.write(line_ + "\n")
    file.write("Winner:" + str(sorted_items[0])+"\n")
    file.write(line_)