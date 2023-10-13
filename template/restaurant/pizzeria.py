from typing import List, Callable, Tuple
from restaurant.nutritional import Nutritional


class Pizzeria:
    def __init__(self) -> None:
        pass

    # R1
    def create_ingredient(self, name: str, carbs: float, fat: float, proteins: float) -> Nutritional:
        pass

    def get_ingredient(self, name: str) -> Nutritional:
        pass

    # R2
    def create_pizza_tray(self, name: str, size: int) -> None:
        pass

    def get_pizza_tray(self, name: str) -> Nutritional:
        pass

    def add_tray_ingredient(self, tray_name: str, ingredient_name: str, pos: Tuple[int, int], size, quantity: float) -> None:
        pass

    def get_slice(self, tray_name: str, pos: Tuple[int, int]) -> List[Nutritional]:
        pass

    def get_layer(self, tray_name: str, num_layer: int) -> List[List[str]]:
        pass

    # R4
    def get_contiguous_portion(self, tray_name: str, pos: Tuple[int, int], to_avoid: str) -> List[List[bool]]:
        pass

    # R5
    def sort_slice(self, tray_name: str, pos: Tuple[int, int], score_func: Callable[[Nutritional], float]) -> List[Nutritional]:
        pass
