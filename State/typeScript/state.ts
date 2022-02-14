class Bank {
  private _instanceState!: IStateAccount;
  private _amount: number = 0;

  constructor(initialState: IStateAccount) {
    this.setState(initialState);
  }

  public get amount(): number {
    return this._amount;
  }
  public set amount(amount: number) {
    this.amount = amount;
  }

  public setState(state: IStateAccount): void {
    console.log(`ahora el estado es  ${(<any>state).constructor.name}`);
    this._instanceState = state;
    this._instanceState.setContext(this);
  }

  buy(amount: number) {
    this._instanceState.buy(amount);
  }

  addAmount(amount: number) {
    this._instanceState.addAmount(amount);
  }

  discount(amount: number) {
    this._amount -= amount;
  }

  deposit(amount: number) {
    this._amount += amount;
  }
}

interface IStateAccount {
  buy(mount: number): void;
  addAmount(mount: number): void;
  setContext(context: Bank): void;
}

class newAccount implements IStateAccount {
  private _context!: Bank;

  setContext(context: Bank) {
    this._context = context;
  }

  addAmount(mount: number): void {
    this._context.deposit(mount);
    this._context.setState(new NoDeudor());
  }

  buy(mount: number): void {
    console.log('No tienes dinero, primero has un deposito');
  }
}

class NoDeudor implements IStateAccount {
  private _context!: Bank;

  buy(mount: number): void {
    if (this._context.amount >= mount) {
      console.log(
        `tengo en el banco ${this._context.amount} y voy a gastar ${mount}`
      );
      this._context.discount(mount);
    } else {
      console.log(
        `no puedes gastar mas de lo que tienes en el banco ${this._context.amount} y quieres gastar ${mount}`
      );
    }

    if (this._context.amount == 0) {
      this._context.setState(new IsDeudor());
    }
  }

  addAmount(mount: number): void {
    this._context.deposit(mount);
    console.log(`ya tienes saldo en tu cuenta :) = ${this._context.amount}`);
  }
  setContext(context: Bank): void {
    this._context = context;
  }
}

class IsDeudor implements IStateAccount {
  private _context!: Bank;

  buy(mount: number): void {
    console.log('no tienes saldo suficiente');
  }
  addAmount(mount: number): void {
    this._context.deposit(mount);
    console.log(`ya tienes saldo en tu cuenta :) = ${this._context.amount}`);
    this._context.setState(new NoDeudor());
  }
  setContext(context: Bank): void {
    this._context = context;
  }
}

const bank = new Bank(new newAccount());
bank.buy(19);
bank.addAmount(100);
bank.buy(10);
bank.buy(100);
bank.addAmount(200);
bank.buy(100);
bank.addAmount(100);
bank.buy(290);
bank.buy(12);
bank.addAmount(100);
bank.buy(100)
