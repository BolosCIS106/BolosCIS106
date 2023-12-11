def loadarrays(lname, salary):
  f = open("myfile.txt", "r")
  for i in range(0, 10, 1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    lname3.append(ln)
    s = f.readline()
    s.rstrip("\n")
    salary.append(s)
  f.close()
def darrays(lname3, salary):
  for i in range (0, 10):
    print(lname[i], "Grade: ", salary[i])
def displayarrays(lname, salary):
  for i in range (0, 10):
    print(lname[i], "Grade : ", salary[i])
    print ("Another Display using for loops")
    for x in range(2, 9, 1):
      print(lname[x])
      for j in lname:
        print(j)

def rdisplay(lname):
  for i in range (9, -1, -1):
    print(lname[i])
    print(lname)
    lname2 = lname[::-1]
    print(lname2)
    lname.reverse()
    print(lname)
lname = ["Adams","Baker", "Clark", "Davis", "Evans", "Frank", "Hills", "Jones" , "George", "Paul"]
Grade = [76, 77, 78, 79, 80, 82, 84, 86, 88, 90]





def displayarrays(lname):
  for i in range (0,10):
    print(lname[i])
  print(" ")
  print("Names In Reverse Order: ")

  for x in range (9, -1,-1):
    print(lname[x])

lname = ["Adams","Baker", "Clark", "Davis", "Evans", "Frank", "Hills", "Jones" , "George", "Paul"]





lname3 = []
salary = []

loadarrays(lname3, salary)
darrays(lname3, salary)