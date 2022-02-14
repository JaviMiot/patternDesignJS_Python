from abc import ABC, abstractmethod


class StateAbstract(ABC):
    @abstractmethod
    def buy(self, cost: float):
        pass

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def setContext(self, context):
        pass


class Context:

    def __init__(self, initState: StateAbstract):
        self.__residue: float = 0.0
        self.setState(initState)

    @property
    def residue(self):
        return self.__residue

    def setState(self, state: StateAbstract):
        self.__state: StateAbstract = state
        print(self.__state)
        self.__state.setContext(self)

    def buySomething(self, cost: float):
        self.__state.buy(cost)

    def depositSalary(self, amount: float):
        self.__state.deposit(amount)

    def _reduce(self, cost: float):
        self.__residue -= cost

    def _add(self, amount: float):
        self.__residue += amount


class IsDeudor(StateAbstract):

    def __init__(self):
        self.__context = None

    def setContext(self, context: Context):
        self.__context = context

    def buy(self, cost: float):
        print("No puedes comprar eres un deudor")

    def deposit(self, amount: float):
        self.__context._add(amount)
        self.__context.setState(NoDeudor())
        print(f'tengo de saldo total {self.__context.residue}')


class NoDeudor(StateAbstract):
    def __init__(self):
        self.__context = None

    def setContext(self, context: Context):
        self.__context = context

    def buy(self, cost: float):
        if(self.__context.residue >= cost):
            self.__context._reduce(cost)
            print(
                f'Realizo una compra de {cost} me queda un saldo total de {self.__context.residue}')
        else:
            print(
                f'Quieres gastar {cost} con tu saldo total de {self.__context.residue}')

        if(self.__context.residue == 0):
            self.__context.setState(IsDeudor())

    def deposit(self, amount: float):
        self.__context._add(amount)
        print(f'tengo de saldo total {self.__context.residue}')


class NewCount(StateAbstract):
    def __init__(self):
        self.__context = None

    def setContext(self, context: Context):
        self.__context = context

    def buy(self, cost: float):
        print('Su cuenta es nueva necesita hacer un deposito inicial primero')

    def deposit(self, amount: float):
        self.__context._add(amount)
        print(f'tengo de saldo total {self.__context.residue}')
        self.__context.setState(NoDeudor())


if __name__ == '__main__':
    context = Context(NewCount())
    context.buySomething(50)
    context.depositSalary(100)
    context.buySomething(50)
    context.buySomething(50)
    context.buySomething(50)
    context.depositSalary(50)
    context.buySomething(55)
    context.buySomething(50)
