class Automobile {
  String color;
  String model;
  String fuel;
  int number_wheels;

  Automobile(this.color, this.model, this.fuel, this.number_wheels);

  void turn_on(String object) {
    print('${object} Ligado');
  }

  void turn_off(String object) {
    print('${object} Desligado');
  }

  void open_window(String object) {
    print('Janela do ${object} aberta');
  }

  void close_window(String object) {
    print('Janela do ${object} fechada');
  }
}

class Car extends Automobile {
  Car(String color, String model, String fuel, int number_wheels)
      : super(color, model, fuel, number_wheels);
}

class Motorcycle extends Automobile {
  Motorcycle(String color, String model, String fuel, int number_wheels)
      : super(color, model, fuel, number_wheels);

  void open_window(String object) {
    print('Uma moto não tem janela');
  }
  
  void close_window(String object) {
    print('Uma moto não tem janela');
  }
}

class Truck extends Automobile {
  Truck(String color, String model, String fuel, int number_wheels)
      : super(color, model, fuel, number_wheels);
}

void main() {
  Car car = Car('blue', 'HB20', 'Gasoline', 4);

  car.turn_on('Carro');
  car.open_window('Carro');
  car.close_window('Carro');
  car.turn_off('Carro');
}
