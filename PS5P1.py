#input phase
qty = float(input("Enter Quantity: "))

#process phase
if qty >= 1000: 
  up = 3.0 
else: up = 5.0 
extprice = qty * up
tax = extprice * 0.07
total = extprice + tax

#output phase
print("Quantity Ordered: " + str(qty))
print("Unit Price: " + str(up)) 
print("Extended Price is: $" + str(extprice))
print("Tax is: $" + str(tax))
print("Total Order: $" + str(total))