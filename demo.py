class student:
    school = "sbmp"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def info(cls):
        return cls.school


s1 = student(12, 23, 34)
s2 = student(11, 22, 33)

print(s1.avg())
print(student.info())
