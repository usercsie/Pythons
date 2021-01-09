print('Hello world')


def SayHelloByFunction():
    print('Hello world by function')


class SayHello:
    def Say(self):
        print('Hello world by class')


SayHelloByFunction()

person = SayHello()
person.Say()
