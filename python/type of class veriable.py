class phone():
    chargertype="c-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("price;",self.price)
        print("chargertype:",self.chargertype)
phone.chargertype="b-type"

samsung=phone("samsung","10000")
samsung.display()

redmi=phone("redmi","5000")
redmi.display()

google=phone("google","50000")
google.display()
