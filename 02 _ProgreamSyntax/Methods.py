class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print('I am an A!')

    # 類別方法
    @classmethod
    def classkids(cls):
        print('class method: A has', cls.count, 'little objects.')

    # 實例方法
    def kids(self):
        print('Instance method: A has', self.count, 'little objects.')

    # 靜態方法
    @staticmethod
    def staticKids():
        print('Static method: A has', A.count, 'little objects.')


# -----------------------------------------------------------------
easy_a = A()
breezy_a = A()
wheezy_a = A()
easy_a.kids()
A.classkids()
A.staticKids()
