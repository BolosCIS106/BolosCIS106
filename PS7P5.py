sumofdiscamt = 0
nooforders = 0
response = input("Do you want to calculate total order with discount? (Yes or No): ") 
while response == "Yes":
  Quanity = float(input("Enter Quanity: "))
  price = float(input("Enter Price: "))
  extprice = Quanity * price
  if extprice > 10000.00:
    discountamt = extprice * 0.25
  else:
    discountamt = extprice * 0.10
    totalorder = extprice - discountamt
    sumofdiscamt = sumofdiscamt + discountamt
    nooforders = nooforders +1
    print("Extended Price: $", extprice)
    print("Discount Amount: $", discountamt)
    print("Total Order Amount: $", totalorder)
    print("Do you want to enter another order (Yes or No)")
    input(response)

nooforders = nooforders + 1
print("Total Discounts Given: $", sumofdiscamt)
print("Number of ordered entered: ", nooforders)
avgdiscamt = sumofdiscamt / nooforders
print("Average Discount: $", avgdiscamt)