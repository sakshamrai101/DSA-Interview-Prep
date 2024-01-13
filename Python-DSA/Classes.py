class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie_1 = Cookie('chocolate_chip')
cookie_2 = Cookie('mint_chocolate')



print("1.", cookie_1.get_color())
print("2.", cookie_2.get_color(), "\n")

cookie_2.set_color('oatmeal_raisin')
print("2.", cookie_2.get_color())