/* ?
 * Se crea el producto complejo
 */

class Car {
  public seats: number = 0;
  public power: number = 0;
  public doors: number = 0;
  public wheels: number = 0;
  public trunk: boolean = false;
  public polarizedGlasses: boolean = false;
  constructor() {}
}

interface ICarBuilder {
  addSeats(number: number): void;
  addPower(number: number): void;
  addDoor(number: number): void;
  addWheels(number: number): void;
  addTrunk(haveTruck: boolean): void;
  addPolarizedGlasses(havePolarized: boolean): void;

  getCar(): Car;
}

class CarBuilder implements ICarBuilder {
  _instance: Car;

  constructor() {
    this._instance = new Car();
  }

  resetCar(): void {
    this._instance = new Car();
  }

  addSeats(number: number): void {
    this._instance.seats = number;
  }
  addPower(number: number): void {
    this._instance.power = number;
  }
  addDoor(number: number): void {
    this._instance.doors = number;
  }
  addWheels(number: number): void {
    this._instance.wheels = number;
  }
  addTrunk(haveTruck: boolean): void {
    this._instance.trunk = haveTruck;
  }
  addPolarizedGlasses(havePolarized: boolean): void {
    this._instance.polarizedGlasses = havePolarized;
  }
  getCar(): Car {
    const car = this._instance;
    this.resetCar();
    return car;
  }
}

class DirectorCar {
  carBuilders: ICarBuilder;
  constructor(builders: CarBuilder) {
    this.carBuilders = builders;
  }

  makeAuto(): void {
    this.carBuilders.addDoor(4);
    this.carBuilders.addPower(1.5);
    this.carBuilders.addSeats(4);
    this.carBuilders.addTrunk(false);
    this.carBuilders.addPolarizedGlasses(false);
    this.carBuilders.addWheels(4);
  }

  makeCamion(): void {
    this.carBuilders.addDoor(2);
    this.carBuilders.addPower(2.5);
    this.carBuilders.addSeats(2);
    this.carBuilders.addTrunk(true);
    this.carBuilders.addPolarizedGlasses(false);
    this.carBuilders.addWheels(6);
  }
}

const ensambladora = new CarBuilder();
const consecionario = new DirectorCar(ensambladora);
consecionario.makeAuto();
const auto = ensambladora.getCar();
consecionario.makeCamion();
const autoCamion = ensambladora.getCar();
console.log(auto);
console.log(autoCamion);
