from Drink import Drink

class Water(Drink):
    def __init__(self, name, price, sampling):
        super().__init__(name, price)
        self.sampling = sampling
        self.note = '採水地：{}'.format(self.sampling)
