class Schoolfee:
    def __init__(self):
        self.__maxprice=1800
        
    def sell(self):
        print("selling price{}".format(self.__maxprice))
        
    def setMaxPrice(self,price):
        self.__maxprice=price
        
        
        
c=Schoolfee()
c.sell()
c.__maxprice=900

c.setMaxPrice(900)
c.sell()