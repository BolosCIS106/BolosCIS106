#input phase
principle = float(input("Enter Principle Amount: $"))

#process phase
if principle > 100000:
  maturity = 5
  irate = 0.06
else:
  if principle > 50000:
    maturity = 10
    irate = 0.05
  else:
    maturity = 15
    irate = 0.04

fyear = principle * irate

#output phase
print("Principle: $", principle)
print("Interest Rate: ", irate)
print("Interest amount for first year: $", fyear)