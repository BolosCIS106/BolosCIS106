#input phase
fixed = float(input("Enter the Fixed Price: $"))
unitprice = float(input("Enter Unit Price: $"))
unitcost = float(input("Enter Unit Cost: $"))

#process phase
diff = unitprice - unitcost
breakeven = fixed / diff

#output phase
print("Break even point:", breakeven)