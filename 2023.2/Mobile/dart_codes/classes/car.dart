class Car {
  String? color;
  int? year;
  String? fuel;
  String? model;

  void print_data() {
    print('Color: ${color}\nYear: ${year}\nFuel: ${fuel}\nModel: ${model}');
  }

  String change_status(String status) {
    return status == 'on' ? 'off' : 'on';
  }

  String close_open_window(String status) {
    return status == 'closed' ? 'open' : 'closed';
  }
}

void main() {
  String statusCar = 'off';
  String statusWindow = 'closed';
  Car myCar = Car();

  myCar.color = 'blue';
  myCar.year = 2023;
  myCar.fuel = 'Water';
  myCar.model = 'HB20';

  myCar.print_data();

  print(statusCar);
  statusCar = myCar.change_status(statusCar);
  print(statusCar);

  print(statusWindow);
  statusWindow = myCar.close_open_window(statusWindow);
  print(statusWindow);
}
