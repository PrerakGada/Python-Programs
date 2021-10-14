english = float(input(" Please enter English Marks: "))
math = float(input(" Please enter Math Marks: "))
computers = float(input(" Please enter Computer Marks: "))
physics = float(input(" Please enter Physics Marks: "))
chemistry = float(input(" Please enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
percentage = (total / 500) * 100

print("Total Marks = %.2f" % total)
print("Marks Percentage = %.2f" % percentage)
p = percentage // 10


def switchp(p):
  switcher = {
    1: 'Student has failed',
    2: 'Student has failed',
    3: 'Student has failed',
    4: 'Student has Passed',
    5: 'Student has passed Second class',
    6: 'Student has passed Higher Second Class',
    7: 'Student has passed First Class',
    8: 'Student has passed Distinction',
    9: 'Student has passed Distinction',
  }
  return switcher.get(p, "Invalid Percentage")


res = switchp(p)
print(res)
