#input phase
books = float(input("Enter # of books:"))
price = float(input("Enter Price of each Book:"))

#process phase
totalb = books * price
if totalb <= 50.00:
 shipping = 25.00
else: shipping = 0.00
total = totalb + shipping
totalb = books * price

#output phase 
print("Books Price: $", totalb)
print("Shipping Charge: $", shipping)
print("Total: $", total)
print("Thank You for Shopping!")