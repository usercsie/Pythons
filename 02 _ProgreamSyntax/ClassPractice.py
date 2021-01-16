# 聚合與組合, 魔術方法
from collections import namedtuple


class Bill():
    def __init__(self, description):
        self.description = description

    def magicMethod(self):
        print('this is a magicMethod of Bill')


class Tail():
    def __init__(self, length):
        self.length = length

    def magicMethod(self):
        print('this is a magicMethod of Tail')


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description,
              'bill and a', self.tail.length, 'tail')
        self.bill.magicMethod()
        self.tail.magicMethod()


a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()

# namedtuple來減化設計
tuDuck = namedtuple('tuDuck', 'bill tail')
duck = tuDuck('wide orange', 'long')
print(duck, duck.bill, duck.tail)

# namedtuple是不可變的, 但可以用_replace至別一個物件
# duck.tail = 'short'
duck2 = duck._replace(bill='wide orange', tail='short')
print(duck2)
