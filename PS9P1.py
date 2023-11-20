def compExtPrice(qty, unitprice):
  extprice = qty * unitprice
  if extprice > 10000.00:
    discamt = extprice * 0.10
  else:
    discamt = 0.0 

  return extprice
totalexprice = 0.0 
r = input("Do you want to compute extended price (Yes or No)?")
while r == "Yes":
  qty = float(input("Enter quantity: "))
  unitprice = float(input("Enter unit price: "))
  extprice = compExtPrice(qty, unitprice)
  totalexprice = totalexprice + extprice
  print("Enter Price is $: ", extprice)
  r = input("Do you want to compute extended price (Yes or No)?")
print("Total Extended Price is $: ", totalexprice)