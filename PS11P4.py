def average_score(score1, score2, score3, handicap):
  sum = score1 + score2 + score3
  average = sum/3
  haverage = (sum + handicap)/3
  return average, haverage

lname = input("Enter Last Name: ")
score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
handicap = float(input("Enter Handicap Score: "))

average, haverage = average_score(score1, score2, score3, handicap)
print("Last Name: ", lname)
print("Average Score: ", average)
print("Average Score with Handicap: ", haverage)