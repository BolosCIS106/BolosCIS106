#input phase
ticker = input("Enter stock ticker symbol") 
amnt = float(input("Enter number of shares"))
price = float(input("Enter price per share"))

#process phase
amnt = amnt * price
ticker = ticker

#output phase
print("Stock: ", ticker )
print("Total amount invested $",amnt)