from typing import List, Callable, Tuple
from restaurant.nutritional import Nutritional, Ingredient, PizzaTray


class Pizzeria:
    def __init__(self) -> None:
        self._ingredients = {}
        self._trays = {}

    # R1
    def create_ingredient(self, name: str, carbs: float, fat: float, proteins: float) -> Nutritional:
        self._ingredients[name] = Ingredient(name, carbs, fat, proteins)
        return self._ingredients[name]

    def get_ingredient(self, name: str) -> Nutritional:
        return self._ingredients[name]

    # R2
    def create_pizza_tray(self, name: str, size: int) -> None:
        self._trays[name] = PizzaTray(name, size)

    def get_pizza_tray(self, name: str) -> Nutritional:
        return self._trays[name]

    def add_tray_ingredient(self, tray_name: str, ingredient_name: str, pos: Tuple[int, int], size, quantity: float) -> None:
        for i in range(size):
            for j in range(size):
                tray = self._trays[tray_name]
                ingredient = self._ingredients[ingredient_name]
                tray.add_ingredient(pos[0]+i, pos[1]+j, ingredient, quantity/size**2)

    def get_slice(self, tray_name: str, pos: Tuple[int, int]) -> List[Nutritional]:
        return self._trays[tray_name].get_slice(*pos)

    def get_layer(self, tray_name: str, num_layer: int) -> List[List[str]]:
        return self._trays[tray_name].get_layer(num_layer)

    # R4
    def get_contiguous_portion(self, tray_name: str, pos: Tuple[int, int], to_avoid: str) -> List[List[bool]]:
        return self._trays[tray_name].get_contiguous_portion(*pos, to_avoid)

    # R5
    def sort_slice(self, tray_name: str, pos: Tuple[int, int], score_func: Callable[[Nutritional], float]) -> List[Nutritional]:
        return sorted(self._trays[tray_name].get_slice(*pos), key=score_func)



