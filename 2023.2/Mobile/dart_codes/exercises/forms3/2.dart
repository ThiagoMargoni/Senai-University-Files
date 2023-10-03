class Automobile {
  String? color;
  String? model;
  String? fuel;
  int? number_wheels;

  Automobile(this.color, this.model, this.fuel, this.number_wheels);

  void turn_on(Object object) {
    print('$object Ligado');
  }

  void turn_off() {}
}

class Car extends Automobile {
  Car(String color, String model, String fuel, int number_wheels)
      : super(color, model, fuel, number_wheels);
}

class Motorcycle extends Automobile {
  Motorcycle(String color, String model, String fuel, int number_wheels)
      : super(color, model, fuel, number_wheels);
}

class Truck extends Automobile {
  Truck(String color, String model, String fuel, int number_wheels)
      : super(color, model, fuel, number_wheels);
}

void main() {}
