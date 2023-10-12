import 'dart:io';

class Machine {
  String name;
  int axes;
  double rpm;
  double energy_consumption;

  Machine(this.name, this.axes, this.rpm, this.energy_consumption);

  void turn_on() => print('Máquina ligada');

  void turn_off() => print('Máquina desligada');

  void change_rotation(double new_rpm) {
    this.rpm = new_rpm;
    print('Nova rotação: ${this.rpm}');
  }
}

class Drill extends Machine {
  Drill(String name, int axes, double rpm, double energy_consumption)
      : super(name, axes, rpm, energy_consumption);
}

void main() {
  Drill drill = Drill('Bosch Drill', 4, 200, 25);

  drill.turn_on();

  while (true) {
    print('Defina o rpm: ');

    double new_rpm = double.parse(stdin.readLineSync()!);
    drill.change_rotation(new_rpm);

    print('Deseja mudar novamente? [S/N] ');
    var res = stdin.readLineSync()!;

    if (res.toUpperCase() == 'N') {
      break;
    }
  }

  drill.turn_off();
}
