class Car {
  String? color;
  int? year;
  String? fuel;
  String? model;

  void print_data() {
    print('Color: ${color}\nYear: ${year}\nFuel: ${fuel}\nModel: ${model}');
  }
}

void main() {
  Car myCar = Car();

  myCar.color = 'blue';
  myCar.year = 2023;
  myCar.fuel = 'Water';
  myCar.model = 'HB20';

  myCar.print_data();
}
