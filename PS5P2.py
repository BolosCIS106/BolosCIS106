#input phase
qty = float(input("Enter Quantity: ")) 
item = input("Enter Item: ")

#process phase
if item == "A" or item == "a":
  unitp = 10.00 
else: unitp = 20.00
extp = qty * unitp

#output phase
print("Unit Price: $", unitp)
print("Extended Price: $", extp)
print("The Item Ordered: ", item)
