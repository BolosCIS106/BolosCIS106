class Student:
  def __init__(self, fname, lname, district_code, enrolled_credits):
      self.fname = fname
      self.lname = lname
      self.district_code = district_code
      self.enrolled_credits = enrolled_credits

  def compute_tuition(self):
      if self.district_code == 'I':
          tuition_rate = 250.00
      else:
          tuition_rate = 500.00

      tuition_owed = self.enrolled_credits * tuition_rate
      return tuition_owed

student1 = Student("Bolos", "Jando", "I", 12)
tuition1 = student1.compute_tuition()
print(f"{student1.fname} {student1.lname} owes ${tuition1:.2f} in tuition.")

student2 = Student("George", "Jando", "O", 15)
tuition2 = student2.compute_tuition()
print(f"{student2.fname} {student2.lname} owes ${tuition2:.2f} in tuition.")