class student:
    def __init__(self):
        self.name=""
        self.redno=""
    def display(self):
        print("name:",self.name)
        print("Reg no :",self.redno)
s1=student()
s2=student()

s1.name="sakthi"
s1.redno="1"

s2.name="sarathi"
s2.redno="2"

s1.display()
s2.display()

