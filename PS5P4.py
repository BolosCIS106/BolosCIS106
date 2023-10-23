#input phase
name = input("Enter Name: ")
cost = float(input("Enter Cost: $"))

#process phase
appliance = cost
if cost >= 1000.00:
  warrantee = .10 * cost
else: warrantee = .05 * cost
total = appliance + warrantee

#output phase
print("Name: ", name)
print("Warrantee Cost: $", warrantee)
print("Total Cost: $", total)
