class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class a")
class b():
    def __init__(self):
        super().__init__()
        print("B")
    def diplay(self):
        print("you are in class b")
class c(b,a):
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("you are in class c")
ob1=c()



