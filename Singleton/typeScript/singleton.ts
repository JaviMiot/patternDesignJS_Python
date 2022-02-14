class Car {
  static _instance: Car;
  color: string;
  capacity: number;

  private constructor(color: string, capacity: number) {
    this.color = color;
    this.capacity = capacity;
  }

  static getInstance(color: string, capacity: number) {
      if(!this._instance){
        this._instance = new Car(color, capacity);
      }
      return this._instance;
  }
}

const c1 = Car.getInstance('red', 5)
const c2 = Car.getInstance('blue', 15)
console.log(c1)
console.log(c2)
console.log(c1==c2)