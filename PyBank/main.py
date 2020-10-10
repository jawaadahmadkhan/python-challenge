#!/usr/bin/env python
# coding: utf-8

import os
import csv


csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

csvfile=open(file=csvpath,newline='')
csvfile.close


months = 0
total = 0
prev_rev = 0
month_of_change = []
rev_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999999999999]

with open(file=csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    
    for i in csvreader:
        months = months + 1
        month = i[0]
        amount = i[1]
        int_amount = int(amount)
        
        #Revenue Change
        rev_change = int(amount) - prev_rev
        prev_rev = int(amount)
        rev_change_list = rev_change_list + [rev_change]
        month_of_change = month_of_change + [month]
        prev_rev = int_amount
        
        #Greatest Increase
        if (rev_change > greatest_increase[1]):
            greatest_increase[0] = month
            greatest_increase[1] = rev_change
        
        #Greatest Decrease
        if (rev_change < greatest_decrease[1]):
            greatest_decrease[0] = month
            greatest_decrease[1] = rev_change
        
        total += int(amount)
        

        
revenue_avg = sum(rev_change_list[1:]) / len(rev_change_list[1:])

output = (
    f'\nFinancial Analysis\n'
    f'-----------------------------\n'
    
    f'Total Months: {months}\n'
    f'Total: $ {total}\n'
    f'Average Change: ${round(revenue_avg,2)}\n'
    f'Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]}\n'
    f'Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]}\n')
    
print(output)


output_path = os.path.join('.','Analysis','budget_analysis.txt')
with open(output_path,"w") as txt_file:
    txt_file.write(output)




