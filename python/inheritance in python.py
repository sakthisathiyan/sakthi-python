class dad():
    def phone(self):
        print("dads phone")
class mom():
    def sweet(self):
        print("moms sweet")
class son(dad,mom):
    def laptop(self):
        print("sons laptop")

ram=son()
ram.phone()
ram.sweet()
