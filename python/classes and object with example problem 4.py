class calculator:
    def __init__(self,a,b):
        self.r1=a
        self.r2=b
    def add(self):
        print(self.r1+self.r2)
    def sub(self):
        print(self.r1-self.r2)
    def mul(self):
        print(self.r1*self.r2)
    def div(self):
        print(self.r1/self.r2)
    
    
s1=calculator(10,2)
s2=calculator(10,2)
s3=calculator(10,2)
s4=calculator(10,2)
s1.add()
s2.sub()
s3.add()
s4.div()
