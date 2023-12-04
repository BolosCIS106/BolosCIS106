def salesreport(sales):
  if sales > 100000:
    percent = .10
  elif sales < 100000:
    percent = .05
  commission = sales * percent

  target = sales * .05
  return commission, target
lname = input("Last Name: ")
sales = float(input("Enter Number of Sales: "))  
commission, target = salesreport(sales)  
print("Last Name: ", lname)
print("Sales: ", commission)  
print("Target: ", target)  