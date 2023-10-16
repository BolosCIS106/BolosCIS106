#input phase 
prchprice = float(input("Enter the purchase price: $"))
crrntprice = float(input("Enter the current price: $"))
qnty = float(input("Enter the Quanity of shares: "))

#process phase
initialamt = prchprice * qnty
nowamt = crrntprice * qnty
amount = nowamt - initialamt

#output phase
print("The profit is: $", amount)