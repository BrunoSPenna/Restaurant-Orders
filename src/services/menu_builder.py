from typing import Dict, List
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"

class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = next(dish for dish in self.menu_data.dishes if dish.name == dish_name)
        except StopIteration:
            raise ValueError("Dish does not exist")
        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu_items = []
        for dish in self.menu_data.dishes:
            if restriction is None or restriction not in dish.get_restrictions():
                if all(ingredient in self.inventory.inventory for ingredient in dish.get_ingredients()):
                    menu_items.append({
                        "dish_name": dish.name,
                        "price": dish.price,
                        "restrictions": list(dish.get_restrictions()),
                        "ingredients": list(dish.get_ingredients()),
                    })
        return menu_items
