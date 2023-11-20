def pay_rate():
  """Calculate gross pay"""
  if code == "L":
    payrate = 25
  else:
    if code == "A":
      payrate = 30
    else:
      if code == "J":
        payrate = 50
      else:
        payrate = 0.0
  return payrate
payrate = 0.0
r = input("Do you want to compute extended price (Yes or No): ")
while r == "Yes":

  lname = input("Enter Last Name: ")
  hours = float(input("Enter hours worked: "))
  code = input("Enter Job Code: ")
  payrate = pay_rate()
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
