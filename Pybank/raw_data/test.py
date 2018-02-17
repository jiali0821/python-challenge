import os
import csv

csvpath = os.path.join("raw_data", "budget_data_1.csv")
date_ori = 0
rev = 0
total_diff = 0
diff_new =[]

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    new_reader = list(csvreader)

    for i, j in enumerate(new_reader):
        date_ori = date_ori + 1
        rev = rev + int(j[1])
    print("Total Month is: "+ str(date_ori))   
    print("Total Revenue is: " + str(rev))




  

    for i, j in enumerate(new_reader):
        if i+1 < date_ori:
            diff = int(new_reader[i+1][1])  - int(new_reader[i][1])
            diff_new.append(diff)
            print(diff_new)
            #diff_2 = int(new_reader[i+2][1])  - int(new_reader[i+1][1])
            '''if abs(diff_2) > abs(diff_1):
                print(diff_2)
            else: 
                print(diff_1)'''
  


     
        
        
      