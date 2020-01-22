# Import Modules
import os 
import csv 

# read the CSV File
pybank_file = os.path.join('Resources', 'budget_data.csv')
with open(pybank_file, 'r', newline='') as pybank_csv:
    csv_reader = csv.reader(pybank_csv, delimiter=",")
    next(csv_reader, None)

    # Reset
    pybank_csv.seek(0)
    next(pybank_csv, None)

    #* The total number of months included in the dataset
    monthCount = 0
    profitLossTotal = 0
    changes_list = []
    for row in csv_reader:
        monthCount = monthCount + 1

    # Reset
    pybank_csv.seek(0)
    next(pybank_csv, None)

        #   * The net total amount of "Profit/Losses" over the entire period
    profitLoss_int = [int(r[1]) for r in csv_reader]
    profitLossTotal = sum(profitLoss_int)

#   * The average of the changes in "Profit/Losses" over the entire period
    changes_list = [profitLoss_int[i+1]-profitLoss_int[i] for i in range(len(profitLoss_int)-1)]
    average = sum(changes_list) / len(changes_list)
    
    # Reset
    pybank_csv.seek(0)
    next(pybank_csv, None)

#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
    maxProfit = max(changes_list)
    minLoss = min(changes_list)
    maxIndex = changes_list.index(maxProfit) + 1
    minIndex = changes_list.index(minLoss) + 1
    dates = [r[0] for r in csv_reader]

# Write
text_file = open("financial_analysis.txt", "w")
text_file.write(f'Financial Analysis \n Total Months: {monthCount} \n Total: {profitLossTotal} \n Average Change: ${average} \n Greatest Increase in Profits: {dates[maxIndex]} ${maxProfit} \n Greatest Decrease in Profits: {dates[minIndex]} ${minLoss}')