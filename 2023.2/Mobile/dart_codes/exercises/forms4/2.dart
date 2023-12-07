import 'dart:ffi';

abstract class IndustrialMachine {
  void name();
  void power();
  void status(bool is_on);
  void turn_on();
  void turn_off();
}

class Press implements IndustrialMachine {
  double pressure;
  Press(this.pressure);

  void name() {
    print('Press 2.0');
  }

  void power() {
    print('The power of Press 2.0 is 100');
  }

  void status(bool is_on) {
    if (is_on = true) {
      print('The machine is os');
    } else {
      print('The machine is off');
    }
  }

  void turn_on() {
    print('Press the button to turn on');
  }

  void turn_off() {
    print('Press the button to turn off');
  }
}

class Robot implements IndustrialMachine {
  String solder;
  Robot(this.solder);

  @override
  void name() {
    print('Robot BMO');
  }

  @override
  void power() {
    print('The power of Robot BMO is 200 ');
  }

  @override
  void status(bool is_on) {
    if (is_on = true) {
      print('The robot is os');
    } else {
      print('The robot is off');
    }
  }

  @override
  void turn_on() {
    print('Press the button on robot head to turn on');
  }

  @override
  void turn_off() {
    print('Press the button on robot head to turn off');
  }
}

class ShippingCompany implements IndustrialMachine {
  Float speed;
  ShippingCompany(this.speed);

  @override
  void name() {
    print('Tecno Import');
  }

  @override
  void power() {
    print('The power of Tecno Import is 10');
  }

  @override
  void status(bool is_on) {
    if (is_on = true) {
      print('The truck is os');
    } else {
      print('The truck is off');
    }
  }

  @override
  void turn_on() {
    print('Put the key and press the button to turn on');
  }

  @override
  void turn_off() {
    print('Remove the key and press the button to turn off');
  }
}
