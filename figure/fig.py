from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod 
    def draw(self,screen):
        pass