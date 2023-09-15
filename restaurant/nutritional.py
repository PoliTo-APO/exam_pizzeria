from abc import ABC, abstractmethod


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
