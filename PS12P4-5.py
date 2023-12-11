def loadarrays(lname, grade):
  f = open("myfile.txt", "r")
  for i in range(0, 10, 1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    lname3.append(ln)
    s = f.readline()
    s.rstrip("\n")
    salary.append(s)
  f.close()
def darrays(lname3, grade):
  for i in range (0, 10):
    print(lname[i], "Grade: ", salary[i])
def displayarrays(lname, grade):
  for i in range (0, 10):
    print(lname[i], "Grade : ", grade[i])
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
def hilow(lname, grade):
  n = len(lname)
  hig = -1.0
  lowg = 99999999.99
  for y in range(0, 1, 1):
    if float(grade[y]) > float(hig):
      hiindex = y
      hig = grade[y]
      if float(grade[y] < float(hig)):
        loindex = y
        lowg = grade[y]
  print("Highest Grade: ", lname[hiindex], Grade[hiindex])
  print("Lowest Grade: ", lname[loindex], Grade[loindex])



def display_player_data(names, averages):
  for name, avg in zip(names, averages):
      print(f"{name}: {avg}")

def search_player(name, names, averages):
  found = False
  for n, avg in zip(names, averages):
      if n == name:
          print(f"{name}: {avg}")
          found = True
          break
  if not found:
      print("Name not found.")

with open("players.txt", "r") as file:
  player_data = [line.split() for line in file.readlines()]

player_names = [item[0] for item in player_data]
batting_averages = [float(item[1]) for item in player_data]
print("\nDisplay Player Data:")
display_player_data(player_names, batting_averages)

while True:
  search_name = input("\nEnter a last name to search (or 'exit' to quit): ")
  if search_name.lower() == 'exit':
      break
  search_player(search_name, player_names, batting_averages)
f = open("myfile.txt", "r")
lname3 = []
salary = []

loadarrays(lname3, salary)
darrays(lname3, salary)
hilow(lname, Grade)


