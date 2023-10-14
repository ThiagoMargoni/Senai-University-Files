class Components {
  String name;
  double value;
  int quantity;

  Components(this.name, this.value, this.quantity);

  void show() => print(
      'Informações do componente: \nNome: ${this.name}, \nValue: ${this.value}, \nQuantity: ${this.quantity}');

  void connect() => print('O valor dos componentes é ${value * quantity}');
}

class Resistor extends Components {
  Resistor(String name, double value, int quantity)
      : super(name, value, quantity);
}

class Capacitor extends Components {
  Capacitor(String name, double value, int quantity)
      : super(name, value, quantity);
}

class Inductor extends Components {
  Inductor(String name, double value, int quantity)
      : super(name, value, quantity);
}

class Diode extends Components {
  Diode(String name, double value, int quantity) : super(name, value, quantity);
}

class Led extends Components {
  Led(String name, double value, int quantity) : super(name, value, quantity);
}

void main() {
  Resistor res = Resistor('200R', 30, 5);
  res.show();
  res.connect();

  Capacitor cap = Capacitor('10uF', 150, 10);
  cap.show();
  cap.connect();
}
