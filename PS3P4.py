#input phase
make = input("Enter Car Brand:")
model = input("Enter Model:")
msrp = float(input("Enter msrp price:"))
discount = float(input("Enter discount:"))

#process phase
discountpercent = msrp * discount
discountprice = msrp - discountpercent
make = make

#output phase
print("Car Brand: ",make)
print("Model: ",model)
print("MSRP PRICE: $",msrp)
print("Discount Percent: ",discount)
print("Amount off Msrp: ",discountpercent)
print("Discounted Price: $",discountprice)