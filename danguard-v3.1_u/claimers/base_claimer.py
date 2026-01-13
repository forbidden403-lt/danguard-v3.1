from abc import ABC, abstractmethod

class BaseClaimer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def claim(self, target_name: str, **kwargs) -> dict:
        pass