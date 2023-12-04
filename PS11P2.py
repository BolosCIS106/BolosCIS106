def avgtotal(exam1, exam2, exam3):
  total = 300
  score = exam1 + exam2 + exam3 
  avg = score/3
  return avg, score

lname = input("Enter Last Name: ")
exam1 = float(input("Enter Exam 1 Score: "))
exam2 = float(input("Enter Exam 2 Score: "))
exam3 = float(input("Enter Exam 3 Score: "))

avg, score = avgtotal(exam1, exam2, exam3)
print("Last Name: ", lname)
print("Exam Score Average: ", avg)
print(f"\nTotal Points: {score}/300")
