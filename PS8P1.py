p = float(input("Enter Principle: "))
r = float(input("Enter Rate: "))
totint = 0.0
print("Year    Beginning Bal    End Balace")

for x in range(1,6,1):
  i = p * r
  totint = totint + i
  endbal = p + i
  print(x,"    ",p, "    ", endbal)
p = endbal

print("Total interest earned", totint)