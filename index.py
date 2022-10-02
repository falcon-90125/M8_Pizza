# class Product:
#     def __init__(self, title, calorific, cost):
#         self.title = title
#         self.calorific = calorific
#         self.cost = cost
class Product:
    def __init__(self, title, calorific, cost):
        if title:
            self.title = title
        else:
            print("Отсутствует значение атрибута title")
        # if not calorific:
        #     pass
        # if not cost:
        #     pass
        self.calorific = calorific
        self.cost = cost
    
class Ingredient:
    def __init__(self, product, weight):
        self.product = product
        self.weight = weight
    
    def get_calorific(self):
        return self.weight / 100 * self.product.calorific

    def get_cost(self):
        return self.weight / 100 * self.product.cost


class Pizza(Product):
    def __init__(self, title, ingredients = []):
        # self.title = super().__init__(self, title, cost=0)
        self.title = title
        self.ingredients = ingredients

    def get_calorific(self):
        sum_ingredients = 0
        for i in self.ingredients:
            sum_ingredients += i.get_calorific()
        return sum_ingredients

    def get_cost(self):
        sum_cost = 0
        for i in self.ingredients:
            sum_cost += i.get_cost()
        return sum_cost

    def __str__(self):
        if len(self.ingredients) < 3:
            print_pizza = f'{self.title} лайт ({self.get_calorific()} kkal) - {self.get_cost()} руб'
        else:
            print_pizza = f'{self.title} ({self.get_calorific()} kkal) - {self.get_cost()} руб'
        return print_pizza


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
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

# # Выводим экземпляр пиццы
print(pizza_margarita)
print(pizza_margarita_light)