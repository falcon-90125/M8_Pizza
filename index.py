# Программа для создания пиццы из ингредиентов с возможностью расчета общей калорийности и себестоимости конечного продукта.

class Product(): # У продукта есть характеристики: название, калорийность и себестоимость. 
    def __init__(self, title, calorific, cost):
        if title == '' or title.isspace(): # Не может быть пустым
            raise ValueError('Отсутствует значение атрибута title')
        else:
            self.title = title # название
        
        if calorific <0: #калорийность. Только положительное число
            raise ValueError('Значение атрибута calorific может быть только положительным')
        else:
            self.calorific = calorific #калорийность
        
        if cost <0: #себестоимость. Только положительное число
            raise ValueError('Значение атрибута cost может быть только положительным')
        else:
            self.cost = cost

class Ingredient: #product - класс Product,  weight - вес
    def __init__(self, product, weight=0):
        self.product = product
        if weight <0: # Только положительное число
            raise ValueError('Значение атрибута weight может быть только положительным')
        else:
            self.weight = weight
    
    def get_calorific(self): #калорийность ингредиента
        return self.weight / 100 * self.product.calorific

    def get_cost(self): #себестоимость ингредиента
        return self.weight / 100 * self.product.cost

class Pizza(Product): # У пиццы есть название и ингредиенты - Список значений класса Ingredient
    def __init__(self, title, ingredients = []):
        super().__init__(title, calorific=0, cost=0) #название берём по методу __init__ от родительского класса Product, чтобы избежать дублирование кода
        self.ingredients = ingredients

    def get_calorific(self): #общая калорийность пиццы
        sum_ingredients = 0
        for i in self.ingredients:
            sum_ingredients += i.get_calorific()
        return sum_ingredients

    def get_cost(self): #общая себестоимости пиццы
        sum_cost = 0
        for i in self.ingredients:
            sum_cost += i.get_cost()
        return sum_cost

    def __str__(self): #выводиться название пиццы, общая калорийность и общая себестоимость
        if len(self.ingredients) < 3: #Если Список значений класса Ingredient меньше 3, то пицца лайт
            print_pizza = f'{self.title} лайт ({self.get_calorific()} kkal) - {self.get_cost()} руб'
        else:
            print_pizza = f'{self.title} ({self.get_calorific()} kkal) - {self.get_cost()} руб'
        return print_pizza


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Томат', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты.
# Для каждого ингредиента указываем продукт, из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
pizza_margarita_light = Pizza('Маргарита', [dough_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)
print(pizza_margarita_light)