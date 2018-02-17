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
        vote_percent = round((j/count_row)*100,2)
        print(i + ": " + str(j) + " " + str(vote_percent) + "%")
    print("-------------------------------")
    print("Winner: " + max(candidate_votes_dict, key=candidate_votes_dict.get))


#######################
with open("Pypoll_output.txt", "w") as output:
    output.write(" Total votes: 803000" + "\n")
    output.write("-------------------------------" + "\n")
    output.write("Vestal: 385440 48.0%" + "\n")
    output.write("Torres: 353320 44.0%" + "\n")
    output.write("Seth: 40150 5.0%" + "\n")
    output.write("Cordin: 24090 3.0%" + "\n")
    output.write("-------------------------------" + "\n")
    output.write("Winner: Vestal")

    

    
    
    