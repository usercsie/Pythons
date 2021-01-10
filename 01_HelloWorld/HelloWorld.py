print('Hello world')


def SayHelloByFunction():
    print('Hello world by function')


class SayHello:
    def Say(self):
        print('Hello world by class')


class SayHelloAtInit:
    def __init__(self, words):
        self.words = words

    def Say(self):
        print(self.words)


class SayHelloAtInit_Derived(SayHelloAtInit):
    def Say(self):
        print(self.words, ' - Derived')


    # ----------------------------------------------------------------------------------
SayHelloByFunction()

person = SayHello()
person.Say()

person = SayHelloAtInit('Hello world by class __init__')
person.Say()

person = SayHelloAtInit_Derived('Hello world by class __init__')
person.Say()
