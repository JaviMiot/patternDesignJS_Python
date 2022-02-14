class Car:

    __instance = None
    __private = False

    def __init__(self, color, capacity):
        if not Car.__private:
            print('this a singleton class')
        else:
            self.color = color
            self.capacity = capacity
            Car.__private = False
            Car.__instance = self

    @staticmethod
    def getInstance(color, capacity):
        if not Car.__instance:
            Car.__private = True
            Car(color, capacity)
        return Car.__instance


c = Car('sdsd', 1)
c1 = Car.getInstance('red', 12)
c = Car('sdsd', 1)
c2 = Car.getInstance('blue', 22)

print(id(c1))
print(id(c2))
print(c1.color)
print(c2.color)
print(c1 == c2)
