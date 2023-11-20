def tuition_owed():
  """all tuition owed"""
  if code == "I":
    cost = 250
  else:
    if code == "O":
      cost = 550
    else:
        cost = 0.0
  return cost
cost = 0.0
r = input("Do you want to compute tuition owed (Yes or No): ")
while r == "Yes":

  lname = input("Enter Last Name: ")
  credit = float(input("Enter credit hours: "))
  code = input("Enter Job Code: ")
  cost = tuition_owed()


  tuition = cost * credit

  print("Last Name: ", lname)
  print("Total Tuition: ", tuition)