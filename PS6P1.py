#input phase 
widgets = float(input("Enter Amount of Widgets: "))

#process phase
if widgets > 10000:
  price = 10.00
else:
  if widgets > 5000:
    price = 20.00
  else:
    price = 30.00
extp = widgets * price
tax = extp * 0.07
total = extp + tax

#output phase
print("Extended Price: $", extp)
print("Tax Amount: $", tax)
print("Total Amount: $", total)