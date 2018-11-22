class Product:
    def __init__(self, name="", price=0.0, discountPercent=0, img = "", id = 0):
            self.name = name
            self.price = price
            self.discountPercent = discountPercent
            self.img = img
            self.id = id

    def getDiscountAmount(self):
        discountAmount = self.price * self.discountPercent / 100
        return round(discountAmount, 2)

    def getDiscountPrice(self):
        discountPrice = self.price - self.getDiscountAmount()
        return round(discountPrice, 2)

class Category:
    def __init__(self,ID = 0, name=""):
            self.ID = ID
            self.name = name

class LineItem:
    def __init__(self, product=None, quantity=1):
            self.product = product
            self.quantity = quantity

    def getTotal(self):
        total = self.product.getDiscountPrice() * self.quantity
        return round(total,2)

    def upQuantity(self):
        self.quantity += 1

    def setQuantity(self, quantity):
        self.quantiy = quantity
       

class Cart:
    def __init__(self):
        self.__lineItems = []

    #def addItem(self, item): #Works for the original console application
     #   self.__lineItems.append(item)

    def getProducts(self):
         products = []
         for item in self.__lineItems:
             products.append(item.product)
         return products

    def addItem(self, product):
        already = False
        for item in self.__lineItems:
            if (product.id == item.product.id):
                already = True
                i = self.__lineItems.index(item)
                self.__lineItems[i].upQuantity()
        if(already == False):
            item = LineItem(product, 1)
            self.__lineItems.append(item)

    #def removeItem(self, index):
     #   self.__lineItems.pop(index)

    def removeItem(self, product):
        for item in self.__lineItems:
            if product.id == item.product.id:
                index = self.__lineItems.index(item)
                self.__lineItems.pop(index)

    def getTotal(self):
        total = 0.0
        for item in self.__lineItems:
            total += item.getTotal()
        return round(total,2)

    def getItemCount(self):
        return len(self.__lineItems)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineItems)-1:
            raise StopIteration         
        self.__index += 1
        lineItem = self.__lineItems[self.__index]
        return lineItem