from abc import ABC, abstractmethod

# * Product


class Pet(ABC):
    @abstractmethod
    def petDo(self, activity: str):
        pass


class DogPet(Pet):

    def __init__(self, labrar: str):
        self.labrar = labrar

    def petDo(self, activity: str):
        print(f'la mascota hace {activity} y {self.labrar}')


class CatPet(Pet):

    def __init__(self, maullar: str):
        self.maullar = maullar

    def petDo(self, activity: str):
        print(f'la mascota hace {activity} y luego {self.maullar}')


# ? Factory

class petFactory(ABC):
    @abstractmethod
    def get_pet(self) -> Pet:
        pass


class DogFactory(petFactory):
    def __init__(self, ladrar: str):
        self.ladrar = ladrar

    def get_pet(self) -> Pet:
        return DogPet(self.ladrar)


class CatFactory(petFactory):
    def __init__(self, maullar):
        self.maullar = maullar

    def get_pet(self) -> Pet:
        return CatPet(self.maullar)


if __name__ == '__main__':
    factoryDog = DogFactory('guauuu grrr guau')
    dog1 = factoryDog.get_pet()
    dog1.petDo('salta alto')

    factoryCat = CatFactory('miiauuu jejejeje')
    cat1 = factoryCat.get_pet()
    cat1.petDo('aruñar')

    cat2 = factoryCat.get_pet()
    cat1.petDo('se arrastra')
