import os 
import csv

totalmonths = 0
totalprofitloss = 0
previousprofit = 0
profitlossdiff = []
greatestincrease = float('-inf')
greatestincreasedate = ""
greatestdecrease = float('inf')
greatestdecreasedate = "" 
differences = [] 


#establish the csv pathway
csvpath = os.path.join('budget_data.csv')
#open the file in the pathway
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    print(csvreader)
    #establish the headers (Date & Profit/Losses)
    csvheader = next(csvreader)
    print(f"Financial Analysis")
    
    totalmonths = 0
    totalprofitloss = 0
    dates = []
    profit = []
    
    for row in csvreader:
        dates.append(row[0])
        profit.append(int(row[1]))

        #calculate the total number of of months in the dataset
        if row != csvheader:
            totalmonths += 1
            totalprofitloss += int(row[1])
            #calculate the total difference of profit/losses
            if totalmonths == 1:
                initialprofitloss =int(row[1])
            else:
                profitlossdiff.append(int(row[1]) - previousprofit)
            previousprofit = int(row[1])
            #calculate the average in profit/losses
            if len(profitlossdiff) > 0:
                avgchange = sum(profitlossdiff) / len(profitlossdiff)
            else: avgchange = 0

            roundednum = round(avgchange, 2)
            #calculate greatest increase in profits
    
            
    for i in range(1, len(profitlossdiff)):
        profitlossdiff.append(int(row[1]) - previousprofit)
        
        greatestincrease = max(profitlossdiff)
        greatestincreaseindex = profitlossdiff.index(greatestincrease)

                
        #calculate greatest decrease in profits 
        greatestdecrease = min(profitlossdiff)
        greatestdecreaseindex = profitlossdiff.index(greatestdecrease)
    
    greatestincreasedate = dates[greatestincreaseindex+1]
    greatestdecreasedate = dates[greatestdecreaseindex+1]


    #print the data
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${totalprofitloss}")
    print(f"Average Change: ${roundednum: .2f}")
    print(f"Greatest Increase in Profits: {greatestincreasedate} (${greatestincrease})")
    print(f"Greatest Decrease in Profits: {greatestdecreasedate} (${greatestdecrease})")
#open and write the data as a text file 
with open("budget_analysis.txt", "w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f"Total Months: {totalmonths}\n")
        txtfile.write(f"Total: ${totalprofitloss}\n")
        txtfile.write(f"Average Change: ${roundednum: .2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatestincreasedate} (${greatestincrease})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatestdecreasedate} (${greatestdecrease})\n")
        
        




