#input phase
from re import IGNORECASE


lname = input("Enter your last name:")
dependents = float(input("Enter # of Dependents: "))
gross = float(input("Enter Gross Income: "))

#process phase
adjustedgross = dependents * 12000
if adjustedgross <= 50000:
    taxrate = .10
else: taxrate = .20
incometax = adjustedgross * taxrate
if incometax < 0:
    incometax = 100.00
else: incometax = incometax
  
#output phase 
print("Last Name: ", lname)
print("Gross Income: $", gross)
print("Number of Dependents:", dependents)
print("Adjusted Gross Income: $", adjustedgross)
print("Income Tax: $", incometax)

