from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod 
    def draw(self,screen):
        pass
    
    @abstractmethod 
    def inside(self,px,py):
        pass
    
    @abstractmethod 
    def run(self,gx,gy):
        pass