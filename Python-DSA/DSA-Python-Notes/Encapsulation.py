class Product:
    def __init__(self):
        self.maxprice = 1000

    def set_price(self, price):
        self.maxprice = price 

    def show_price(self):
        print(f"The selling price is: {self.maxprice}")


prod1 = Product()
prod1.maxprice = 50
prod1.show_price()

prod1.set_price(75)
prod1.show_price()
