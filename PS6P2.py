#input phase
pnumber = float(input("Enter Part Number: "))
quanity = float(input("Enter Quanity: "))

#process phase
if pnumber == 55:
  price = 1.00
else:
  if pnumber == 10:
    price = 1.00
  else:
    if pnumber == 99:
      price = 2.00
    else:
      if pnumber == 80:
        price = 3.00
      else:
        if pnumber == 70:
          price = 3.00
        else: 
          price = 5.00

total = quanity * price


#output phase:
print("Part Number: ", pnumber)
print("Cost Per Unit: $", price)
print("Total Cost: $", total)
print("Thank You!")