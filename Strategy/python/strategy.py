from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def calculate(self, number1: float, number2: float) -> float:
        pass


class Sum(Operation):

    def calculate(self, number1: float, number2: float) -> float:
        return number1 + number2


class Rest(Operation):

    def calculate(self, number1: float, number2: float) -> float:
        return number1 - number2


class MathOperation(ABC):

    def __init__(self, instance: Operation):
        self.__instance = instance

    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, instance: Operation):
        self.__instance = instance

    def calculate(self, number1: float, number2: float) -> float:
        return self.__instance.calculate(number1, number2)


if __name__ == '__main__':
    mathOperators = MathOperation(Sum())
    print(mathOperators.instance)
    print(mathOperators.calculate(1, 2))
    mathOperators.instance = Rest()
    print(mathOperators.instance)
    print(mathOperators.calculate(1, 2))
