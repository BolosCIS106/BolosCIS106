counter = 0
totalex1 = 0.0

response = input("Want to calculate average score Yes or No: ")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter Student Last Name: ")
  score1 = float(input("Enter Exam Score 1: "))
  score2 = float(input("Enter Exam Score 2: "))
  avg = (score1 + score2)/2
  print(lastname, "has average Score of: ",avg)
  totalex1 = totalex1 + score1
  response = input("Want to calculate average score Yes or No: ")

avgex1 = totalex1 / counter
print ("Number of students: ", counter)
print ("Average Exam Score 1 ", avgex1)