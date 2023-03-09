class Pizza:
    # Encapsulation
    def __init__(self,description, money):
        self.__description=description
        self.__money=money
    def get_description(self):
        return self.__description
    def get_cost(self):
        return self.__money

#Inheritance
class Margarita(Pizza):
    def __init__(self, description="Description of Margarita Pizza", money=100):
         super().__init__(description,money)
class Turk_Pizza(Pizza):
    def __init__(self, description="Description of Turk Pizza", money=120):
         super().__init__(description,money)
class Classic(Pizza):
    def __init__(self, description="Description of Classic Pizza", money=130):
         super().__init__(description,money)
class Plain(Pizza):
    def __init__(self, description="Description of Plain Pizza", money=140):
         super().__init__(description,money)


class Sauce():
    # Encapsulation
    def __init__(self,description, money):
        self.__description=description
        self.__money=money
    def get_description(self):
        return self.__description
    def get_cost(self):
        return self.__money

#Inheritance
class Olives(Sauce):
    # each sauce must have its own price and description of the pizzas as variables.
    def __init__(self, description="Description of Olives",money=10):
        super().__init__(description, money)
        print("Pizzanın costu",Pizza.get_cost(self))
class Mushrooms(Sauce):
    # each sauce must have its own price and description of the pizzas as variables.
    def __init__(self, description="Description of Mushrooms",money=10):
        super().__init__(description, money)

class Goat_Cheese(Sauce):
    # each sauce must have its own price and description of the pizzas as variables.
    def __init__(self, description="Description of Goat Cheese",money=10):
        super().__init__(description, money)

class Meat(Sauce):
    # each sauce must have its own price and description of the pizzas as variables.
    def __init__(self, description="Description of Meat",money=10):
        super().__init__(description, money)

class Onions(Sauce):
    # each sauce must have its own price and description of the pizzas as variables.
    def __init__(self, description="Description of Onions",money=10):
        super().__init__(description, money)

class Corn(Sauce):
    # each sauce must have its own price and description of the pizzas as variables.
    def __init__(self, description="Description of Corn",money=10):
        super().__init__(description, money)


class Decorator():
    def __init__(self,pizza,component):
        self.component=component
        self.pizza=pizza

    def get_cost(self):
        print("\nPizza Price: ",self.pizza.get_cost(),"\nSauce Price: ",self.component.get_cost(),"\n-------------------")
        return self.component.get_cost()+self.pizza.get_cost()

    def get_description(self):
        return self.component.get_description()+" \n "+self.pizza.get_description()

