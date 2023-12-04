total = 0.0
tax = 0.0
def comptotal(qty, price):
  global total
  total = qty * price
  global tax
  tax = total * 0.07
  return

qty = float(input("Enter Quanity: "))
price = float(input("Enter Price: "))
comptotal(qty, price)
print("Total: ", total)
print("Tax Cost: $", tax)