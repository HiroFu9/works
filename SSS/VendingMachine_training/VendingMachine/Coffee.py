from Drink import Drink

class Coffee(Drink):
    def __init__(self, name, price, beenFrom):
        super().__init__(name, price)
        self.beenFrom = beenFrom
        self.note = '豆原産地：{}'.format(self.beenFrom)
