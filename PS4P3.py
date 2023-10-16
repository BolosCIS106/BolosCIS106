#input phase
total = float(input("Enter Total Amount: $"))

#process phase
firsttip = total * .15
tip1 = total + firsttip
secondtip = total * .18
tip2 = total + secondtip
thirdtip = total * .20
tip3 = total + thirdtip

#output phase
print("With 15% Tip")
print("Total: $", total)
print("Tip: $", firsttip)
print("Total With Tip: $", tip1)
print("With 18% Tip")
print("Total: $", total)
print("Tip: $", secondtip)
print("Total With Tip: $", tip2)
print("With 20% Tip")
print("Total: $", total)
print("Tip: $", thirdtip)
print("Total With Tip: $", tip3)