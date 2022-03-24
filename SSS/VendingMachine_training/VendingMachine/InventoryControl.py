class InventoryControl:
    def __init__(self, size):
        self.list = [None] * size  # 飲み物リスト
        self.count = 0             # 登録数

    def getIndex(self, name):
        '項目の位置を取得する'
        for i in range(self.count):
            if self.list[i].name == name:
                return i
        return -1

    def add(self, entry):
        '商品登録'
        if self.count >= len(self.list):
            print('これ以上登録できません。')
            return
        if self.getIndex(entry.name) != -1:
            print('{}は既に登録されています。'.format(entry.name))
            return
        self.list[self.count] = entry
        self.count += 1

    def addStock(self, name, amount):
        '在庫'
        idx = self.getIndex(name)

        if idx == -1:
            print('{}が見つかりません。'.format(name))
            return
        self.list[idx].stock += amount

    def setInitStock(self, amount):
        '初期在庫数設定'
        for i in range(self.count):
            self.list[i].stock = amount

    def dispGoodsList(self):
        '商品一覧表示'
        print()
        print('◆◆ 商品表示 ◆◆')
        for i in range(self.count):
            print()
            print('({}) {}'.format(i + 1, self.list[i].name), end='')
            print(' \t{}円'.format(self.list[i].price), end='')
            print(' （ {} ）'.format(self.list[i].note))
        print()

    def buying(self, money, goodsNo):
        '商品購入'
        stock = self.list[goodsNo - 1].stock
        if stock <= 0:
            print('\n在庫がありません。')
            return -1

        price = self.list[goodsNo - 1].price
        if money < price:
            print('\nお金が不足しています。')
            return -1
        change = money - price
        self.list[goodsNo - 1].stock -= 1
        print('\n【{}】を購入しました。'.format(self.list[goodsNo - 1].name))
        return change

    def dispStockList(self):
        '在庫表示'
        print()
        print('◆◆ 商品在庫 ◆◆')
        for i in range(self.count):
            print()
            print('({}) {}'.format(i + 1, self.list[i].name), end='')
            print(' ・・・・{}本'.format(self.list[i].stock))
        print()
