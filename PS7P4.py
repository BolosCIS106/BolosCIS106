print("Do you want to compute employees gross pay? (Yes or No)")
response = input()
while response == "Yes":
  lname = input()
  hours = float(input("Enter Hours Worked: "))
  print("Enter Rate of Pay: ")
  payrate = float(input())
  if hours > 40:
    baseamt = 40 * payrate
  overtime = hours - 40
  timehalf = payrate + payrate/2
  bonus = overtime * timehalf
  baseamt = 40 * payrate
  gross = baseamt + bonus
  print("Last Name: ", lname)
  print("Hours worked: ",hours)
  print("Rate of Pay: ", payrate)
  print("Overtime Hours: ", overtime)
  print("Pay Rate for overtime: ", timehalf)
  print("Gross Income ", gross)
else:
  gross = hours * payrate
print("Last Name: ", lname)
print("Hours Worked: ", hours)
print("Rate of Pay: ", payrate)
print("Gross Pay: ", gross)