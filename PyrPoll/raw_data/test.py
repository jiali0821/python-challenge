import os
import csv
count_row = 0
#candidateList = []
candidate_votes_dict = {}

csvpath = os.path.join("raw_data", "election_data_1.csv")

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    for voteid, county, candidate in csvreader:
        count_row += 1
        #count_row = count_row + 1
        #if m not in candidateList:
            #candidateList.append(m)
    #print(candidateList)
    #print("Total votes: " + str(count_row))


        if candidate not in candidate_votes_dict.keys():
            candidate_votes_dict[candidate] = 1
        else:
            candidate_votes_dict[candidate] +=1


    print("Total votes: " + str(count_row))
    print("-------------------------------")

    for i, j in candidate_votes_dict.items():
        vote_percent = (j/count_row)*100
        print(i + ": " + str(j) + " " + str(vote_percent) + "%")

#######################
'''with open("Pypoll_output.txt", "w") as output:
    output.write("Total votes: " + str(count_row) + "\n")
    output.write("-------------------------------" + "\n")
    output.write(i + ": " + str(j) + " " + str(vote_percent) + "%" + "\n")
    output.write("-------------------------------" + "\n")
    output.write ("Winner: " + max(candidate_votes_dict))'''

    

    
    
    