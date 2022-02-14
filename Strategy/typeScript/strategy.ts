interface IOperation {
  calculate(number1: number, number2: number): number;
}

class Sum implements IOperation {
  calculate(number1: number, number2: number): number {
    console.log('add');
    return number1 + number2;
  }
}

class Diff implements IOperation {
  calculate(number1: number, number2: number): number {
    console.log('diff');
    return number1 - number2;
  }
}

class Multi implements IOperation {
  calculate(number1: number, number2: number): number {
    console.log('multi');
    return number1 * number2;
  }
}

class Divide implements IOperation {
  calculate(number1: number, number2: number): number {
    console.log('div');
    return number1 / number2;
  }
}

class MathOperations {
  private _instance: IOperation;
  constructor(instance: IOperation) {
    this._instance = instance;
  }

  public set instance(value: IOperation) {
    this._instance = value;
  }

  execute(number1: number, number2: number) {
    return this._instance.calculate(number1, number2);
  }
}

const mathOperations = new MathOperations(new Sum());
console.log(mathOperations.execute(1, 2));
mathOperations.instance = new Diff();
console.log(mathOperations.execute(1, 2));
mathOperations.instance = new Multi();
console.log(mathOperations.execute(4, 2));
mathOperations.instance = new Divide();
console.log(mathOperations.execute(3, 2));
