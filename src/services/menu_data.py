import csv
from typing import Set

from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self.ingredients: Set[Ingredient] = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Ignorar o cabeçalho do CSV
            for row in reader:
                dish_name, price, ingredient_name, quantity = row
                price = float(price)
                quantity = int(quantity)

                dish = self._get_or_create_dish(dish_name, price)
                ingredient = self._get_or_create_ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, quantity)

    def _get_or_create_dish(self, name: str, price: float) -> Dish:
        existing_dish = next(filter(lambda dish: dish.name == name, self.dishes), None)
        if existing_dish:
            return existing_dish
        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish



    def _get_or_create_ingredient(self, name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient
        new_ingredient = Ingredient(name)
        self.ingredients.add(new_ingredient)
        return new_ingredient
