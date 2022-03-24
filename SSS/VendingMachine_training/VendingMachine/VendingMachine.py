from InventoryControl import InventoryControl
from Coffee import Coffee
from Water  import Water
from Tea    import Tea

MAX_ENTRY  = 100  # 最大登録数
INIT_STOCK =  30  # 各初期在庫数

class VendingMachine:
    def __init__(self):
        self.inv = InventoryControl(MAX_ENTRY)
        self.moneyFromCustomer = 0  # お客から預かったお金

    def main(self):
        '自動販売機のシステム'
        self.inv.add(Coffee('BOSS RAINBOW', 130, 'コロンビア'))
        self.inv.add(Coffee('BOSS PREMIUM', 130, 'グアテマラ'))
        self.inv.add(Water('エ ビ ア ン', 100, 'フランス'))
        self.inv.add(Water('おいしい天然水', 120, '富士山麓'))
        self.inv.add(Tea('綾鷹 あやたか ', 180, '緑茶'))
        self.inv.add(Tea('爽 健 美 茶', 180, 'ブレンド茶'))

        self.inv.setInitStock(INIT_STOCK)
        while True:
            print('\n\n◆◆　操作メニュー　◆◆')
            print('\n(1) 商品を購入する')
            print('\n(2) 在庫を確認する')
            print('\n(3) 終了')
            s = self.inputString_menu('\n番号を入力してください。>')

            no = int(s)
            if no == 1:
                self.buying()
            elif no == 2:
                self.inv.dispStockList()
                self.inputEnter('\n表示を確認してください。[Enter]>')
            else:
                return

    def buying(self):
        '商品を購入する'
        money = 0
        while True:
            self.inv.dispGoodsList()  # main()より移動（連続購入時に再度商品一覧表示のため）

            s1 = self.inputString_money('\nお金を投入してください。（残金{}円） >'.format(money))  # 編集済み
            money += int(s1)
            self.moneyFromCustomer = money

            s2 = self.inputString_goods('\n商品番号を選択してください。>')
            goods = int(s2)

            # 商品購入
            change = self.inv.buying(self.moneyFromCustomer, goods)

            if change < 0:
                continue

            self.moneyFromCustomer = money - change  # 自販機のお金を減額
            money = change
            print('\n商品をお取りください。')
            s3 = self.inputString_yes_no('\n追加購入しますか？（はい【1】／いいえ【2】）>')
            if s3 == '1':
                continue
            elif s3 == '2':
                print('\nおつりは')
                if change != 0:
                    print('{}円です。'.format(change))
                    self.inputEnter('\nお受け取りください。[Enter]>')
                else:
                    print('ありません。')
                break

    # 操作メニューの入力制限（1,2,3のいずれか）
    def inputString_menu(self, prompt):
        while True:
            line = input(prompt)
            if line in ['1', '2', '3']:
                return line

    # 投入金額の入力制限（0以上の整数）
    def inputString_money(self, prompt):
        while True:
            line = input(prompt)
            if str.isdecimal(line):
                return line

    # 商品選択の入力制限（商品一覧のいずれかの番号）
    def inputString_goods(self, prompt):
        while True:
            line = input(prompt)
            if str.isdecimal(line) and 1 <= int(line) <= self.inv.count:
                return line

    # はい／いいえの入力制限（1または2）
    def inputString_yes_no(self, prompt):
        while True:
            line = input(prompt)
            if line in ['1', '2']:
                return line

    def inputEnter(self, prompt):
        'Enterキーを入力する'
        input(prompt)

vendingMachine = VendingMachine()
vendingMachine.main()
