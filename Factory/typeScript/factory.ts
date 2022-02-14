/**
 * !
 * Crear una fabrica de Mascotas
 *
 */

abstract class PetCreator {
  abstract createPet(): IPet;
}

class CreateDog extends PetCreator {
  ladrido: string;

  constructor(ladrido: string) {
    super();
    this.ladrido = ladrido;
  }

  createPet(): IPet {
    return new Dog(this.ladrido);
  }
}

interface IPet {
  type: string;
  age: number;
  caracteristic: string;

  walk(): string;
  jump(): string;
  eat(): string;
}

class Dog implements IPet {
  type: string = '';
  age: number = 0;
  caracteristic: string;

  constructor(caracteristic: string) {
    this.caracteristic = caracteristic;
  }

  setAge(value: number) {
      this.age = value;
  }

  walk(): string {
    return `camina y ${this.caracteristic}`;
  }
  jump(): string {
    return `salta y ${this.caracteristic}`;
  }
  eat(): string {
    return `come y ${this.caracteristic}`;
  }
}

const dogCreator = new CreateDog('guaaauu gr gr')
const dogCreatorBilingual = new CreateDog('guaaauu gr gr helooo!')
const dog = dogCreator.createPet()
const dogBilingual = dogCreatorBilingual.createPet()
console.log(dog.eat())
console.log(dogBilingual.eat())
