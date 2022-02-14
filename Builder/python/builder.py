from abc import ABC, abstractmethod


class House:

    def __init__(self):
        self.doors: int = None
        self.windows: int = None
        self.typeOfRoof: str = None
        self.typeOfDoors: str = None
        self.firePlace: bool = None


class BuilderHouse(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def addDoor(self, numberOfDoors: int):
        pass

    @abstractmethod
    def addWindows(self, numberOfWindows: int):
        pass

    @abstractmethod
    def addTypeOfDoors(self, materials: str):
        pass

    @abstractmethod
    def addTypeOfRoof(self, materials: str):
        pass

    @abstractmethod
    def addFirePlaces(self, haveFirePlaces: bool):
        pass

    @abstractmethod
    def getHouse(self):
        pass


class BuilderSimpleHouse(BuilderHouse):

    def __init__(self):
        self.reset()

    def reset(self):
        self.__instance = House()

    def addDoor(self, numberOfDoors: int):
        self.__instance.doors = numberOfDoors

    def addWindows(self, numberOfWindows: int):
        self.__instance.windows = numberOfWindows

    def addTypeOfDoors(self, materials: str):
        self.__instance.typeOfDoors = materials

    def addTypeOfRoof(self, materials: str):
        self.__instance.typeOfRoof = materials

    def addFirePlaces(self, haveFirePlaces: bool):
        self.__instance.firePlaces = haveFirePlaces

    def getHouse(self):
        house = self.__instance
        self.reset()
        return house


class Director:

    def __init__(self, builder: BuilderSimpleHouse):
        self.__instance: BuilderSimpleHouse = builder

    def createWoodHouse(self):
        self.__instance.addDoor(3)
        self.__instance.addWindows(3)
        self.__instance.addTypeOfDoors('wood')
        self.__instance.addTypeOfRoof('wood')
        self.__instance.addFirePlaces(True)

    def createRockHouse(self):
        self.__instance.addDoor(2)
        self.__instance.addWindows(4)
        self.__instance.addTypeOfDoors('rock')
        self.__instance.addTypeOfRoof('rock')
        self.__instance.addFirePlaces(False)


if __name__ == '__main__':
    builder = BuilderSimpleHouse()
    director = Director(builder)

    director.createWoodHouse()
    houseWood1 = builder.getHouse()
    print(houseWood1)
    print(houseWood1.doors)

    director.createWoodHouse()
    houseWood2 = builder.getHouse()
    print(houseWood2)
    print(houseWood2.doors)

    director.createRockHouse()
    houseRock1 = builder.getHouse()
    print(houseRock1)
    print(houseRock1.doors)
