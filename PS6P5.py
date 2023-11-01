#input phase
lname = input("Enter Employee Last Name: ")
level = float(input("Eneter Employee Level: "))
salary = float(input("Enter Employee Salary: "))

#process phase
if level >= 10:
  bonusrate = 0.25
else:
  if level >= 5:
    bonusrate = .20
  else:
    bonusrate = .10

bonus = bonusrate * salary
salarybonus = salary + bonus

#output phase
print("Employee Last Name: ", lname)
print("Bonus Rate:", bonusrate)
print("Bonus Amount: $", bonus)
print("Salary: $", salary)
print("Total Salary: $", salarybonus)