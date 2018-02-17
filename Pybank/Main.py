import os
import csv

csvpath = os.path.join("raw_data", "budget_data_1.csv")
date_ori = 0
rev = 0
total_diff = 0
diff_new =[]

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    new_reader = list(csvreader)

    for i, j in enumerate(new_reader):
        date_ori = date_ori + 1
        rev = rev + int(j[1])
    print("Total Month is: "+ str(date_ori))   
    print("Total Revenue is: " + str(rev))


    for i, j in enumerate(new_reader):
        if i+1 < date_ori:
            diff = int(new_reader[i+1][1])  - int(new_reader[i][1])
            total_diff = total_diff + diff
            avg_diff = round(total_diff/date_ori,2)
            diff = int(new_reader[i+1][1])  - int(new_reader[i][1])
            diff_new.append(diff)
    print("Average Revenue Change is: " + str(avg_diff))
    #print(diff_new)

    diff_abs =[]

    for i in diff_new:
        diff_abs.append(abs(i))
    
    x_1 = min(diff_abs)
    x_2 = diff_abs.index(x_1)
    y_1 = max(diff_abs)
    y_2 = diff_abs.index(y_1)

    print("Greatest Decrese in Revenue:" + str(new_reader[x_2 + 1][0]) + 
    ", $"+ str(diff_new[x_2]))


    print("Greatest Increase in Revenue:" + str(new_reader[y_2 + 1][0]) + 
    ", $"+ str(diff_new[y_2]))


####################################
with open("Pybank_output.txt", "w") as output:
    output.write("Total Month is: "+ str(date_ori) + "\n")
    output.write("Total Revenue is: " + str(rev) + "\n")
    output.write("Average Revenue Change is: " + str(avg_diff) + "\n")
    output.write("Greatest Decrese in Revenue:" + str(new_reader[x_2 + 1][0]) + 
    ", $"+ str(diff_new[x_2]) + "\n")
    output.write ("Greatest Increase in Revenue:" + str(new_reader[y_2 + 1][0]) + 
    ", $"+ str(diff_new[y_2]))


  