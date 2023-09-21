class Car {
  String? brand;
  String? model;
  int? year;
  bool is_on = false;

  void turn_on() {
    if (!is_on) {
      this.is_on = true;
    } else {
      print('O carro já está ligado');
    }
  }

  void turn_off() {
    if (is_on) {
      this.is_on = false;
    } else {
      print('O carro já está desligado');
    }
  }

  void status_engine() {
    if (is_on) {
      print('O carro está ligado');
    } else {
      print('O carro está desligado');
    }
  }
}

void main() {
  Car car = Car();

  car.status_engine();
  car.turn_on();
  car.status_engine();
  car.turn_off();
  car.status_engine();
}
