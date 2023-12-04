def discount(qty, price, discrate):
  total = (qty * price)
  disamt = discrate * total
  discprice = total - disamt

  return disamt, discprice

qty = float(input("Enter The Quanity: "))
price = float(input("Enter the unit price: $"))
discrate = float(input("Enter the discount rate (Use Decimal %): "))
discamt,discprice = discount(qty, price, discrate)

print("Quanity: ", qty)
print("Unit Price: $", price)
print("Discounted Amount: $", discamt)
print("Discounted Price: $", discprice)