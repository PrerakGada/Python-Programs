class Computer:

    def __init__(self):
        self.name = 'Prerak'
        self.age = 17
        
    def update(self):
        self.name = 'Ghost'
        self.age = 18 

c1 = Computer()
c2 = Computer()

print(c1.name)
print(c1.age)
c2.update()
print(c2.name)
print(c2.age)
