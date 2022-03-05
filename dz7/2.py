from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def rasch(ABS):
        pass

    # @property
    # def square(self):
    #     return (self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3)

class Coat(Clothes):


    @property
    def rasch(self):
        return self.param / 6.5 + 0.5

class suit(Clothes):


    @property
    def rasch(self):
        return self.param * 2 + 0.3

#clothes_r = Clothes(4,52)
Suit_r = suit(4)
Coat_r = Coat(52)
print(suit)
print(Coat)
print(f'Площадь ткани на костюм {Suit_r.rasch}')
print(f'Площадь ткани на пальто {Coat_r.rasch}')
print(f'Общая площаль ткани {Suit_r.rasch + Coat_r.rasch} ')
#print(f'Общая площадь ткани {Clothes.square}')