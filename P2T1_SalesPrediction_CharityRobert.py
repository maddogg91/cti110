#CTI-110
#P2T1 - Sales Prediction
#Robert Charity II
#June 12, 2018
#

#User enters Projected Sales as a float
totalSales= float(input("Enter the projected amount of total sales: "))


#Annual Profit is defined as Projected Total Sales multiplied by 23%
annualProfit= totalSales * .23

#Program displays Annual Profit, from the inputted amount
print ("Your annual profit is: ", "$",annualProfit, "From the amount: ", "$",totalSales) 

#Allows user to review their output and quit on the prompt when ready
print ("Press enter key to quit")

input()

