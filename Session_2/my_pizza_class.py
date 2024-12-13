

class Pizza(object):
    def __init__(self,
                 size: int,
                 toppings: list,
                 sauce: str, 
                 crust: str):
        self.size = size
        self.toppings = toppings
        self.sauce = sauce
        self.crust = crust
    

    def add_topping(self, topping: str):
        self.toppings.append(topping)

    
