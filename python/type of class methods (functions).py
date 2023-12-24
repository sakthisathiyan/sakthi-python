class laptop():
    chargertype="c-type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod
    def changechargertype(cls):
        cls.changechargertype="b-type"
        print("charger type changeed to b")
    @staticmethod
    def info():
        print("this is laptop class")

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype()

hp.info()
              
