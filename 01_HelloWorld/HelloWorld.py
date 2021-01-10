import LoggerHelper

print('Hello world')


def sayHelloByFunction():
    print('Hello world by function')


class SayHello:
    def say(self):
        self.__name = 'SayHallo'
        print('Hello world by class')

    @property
    def name(self):
        'get name property'
        return self.__name

    @name.setter
    def name(self, input_name):
        'set name property'
        self.__name = input_name


class SayHelloAtInit:
    def __init__(self, words):
        self.name = 'SayHelloAtInit'
        self.words = words

    def say(self):
        print(self.words)


class SayHelloAtInit_Derived(SayHelloAtInit, LoggerHelper.Dumper):
    def say(self):
        super().say()
        self.name = 'SayHelloAtInit_Derived'
        print(self.words, ' - Derived')


    # ----------------------------------------------------------------------------------
sayHelloByFunction()

person = SayHello()
person.say()

person = SayHelloAtInit('Hello world by class __init__')
person.say()

person = SayHelloAtInit_Derived('Hello world by class __init__')
person.say()

person.dump()
person.name = 'SayHelloAtInit_Derived_changed'
person.dump()
