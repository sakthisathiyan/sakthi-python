class teacher:
    def __init__(self,name,register):
        self.name=name
        self.register=register
    def display(self):
        print("name:",self.name)
        print("register:",self.register)
        
t1=teacher("sakthi","23")
t2=teacher("sarathy","32")

t1.display()
t2.display()
        
