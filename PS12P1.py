def displayarrays(lname):
  for i in range (0,10):
    print(lname[i])
  print(" ")
  print("Names In Reverse Order: ")

  for x in range (9, -1,-1):
    print(lname[x])

lname = ["Adams","Baker", "Clark", "Davis", "Evans", "Frank", "Hills", "Jones" , "George", "Paul"]


displayarrays(lname)