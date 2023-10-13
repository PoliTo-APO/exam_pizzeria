from abc import ABC, abstractmethod
from restaurant.exceptions import TrayException


class Nutritional(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def carbs(self) -> float:
        pass

    @property
    @abstractmethod
    def fat(self) -> float:
        pass

    @property
    @abstractmethod
    def proteins(self) -> float:
        pass


class Food(Nutritional):
    def __init__(self, name, carbs, fat, proteins):
        self._name = name
        self._carbs = carbs
        self._fat = fat
        self._proteins = proteins

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def carbs(self):
        return self._carbs

    @carbs.setter
    def carbs(self, carbs):
        self._carbs = carbs

    @property
    def fat(self):
        return self._fat

    @fat.setter
    def fat(self, fat):
        self._fat = fat

    @property
    def proteins(self):
        return self._proteins

    @proteins.setter
    def proteins(self, proteins):
        self._proteins = proteins


class Ingredient(Food):
    def __lt__(self, other) -> bool:
        return self.name < other.name

    def __str__(self) -> str:
        return "{} {:.2f} {:.2f} {:.2f}".format(self.name, self.carbs, self.fat, self.proteins)


class PizzaTray(Food):
    def __init__(self, name, size):
        super().__init__(name, 0, 0, 0)
        self._ingredients = [[[] for _ in range(size)] for _ in range(size)]

    def __len__(self):
        return len(self._ingredients)

    def add_ingredient(self, x, y, ingredient, quantity):
        if not (0 <= x < len(self) and 0 <= y < len(self)):
            raise TrayException("Ingredient outside boundaries")
        self._ingredients[x][y].append(ingredient)
        self.fat += ingredient.fat / 100 * quantity
        self.carbs += ingredient.carbs / 100 * quantity
        self.proteins += ingredient.proteins / 100 * quantity

    def get_slice(self, x, y):
        return self._ingredients[x][y]

    def get_layer(self, num_layer):
        ingredients = [[None for _ in range(len(self))] for _ in range(len(self))]
        for i in range(len(self)):
            for j in range(len(self)):
                if num_layer < len(self._ingredients[i][j]):
                    ingredients[i][j] = self._ingredients[i][j][num_layer].name
                else:
                    ingredients[i][j] = None
        return ingredients

    def get_contiguous_recursive(self, x, y, to_avoid, selection):
        if selection[x][y] or to_avoid in [i.name for i in self._ingredients[x][y]]:
            return
        selection[x][y] = True
        for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= x + i < len(self) and 0 <= y + j < len(self):
                self.get_contiguous_recursive(x + i, y + j, to_avoid, selection)

    def get_contiguous_portion(self, x, y, to_avoid):
        selection = [[False] * len(self) for _ in range(len(self))]
        self.get_contiguous_recursive(x, y, to_avoid, selection)
        return selection
