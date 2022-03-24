from Drink import Drink

class Tea(Drink):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind
        self.note = '種類：{}'.format(self.kind)
