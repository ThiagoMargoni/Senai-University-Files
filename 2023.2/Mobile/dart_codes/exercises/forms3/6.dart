class Products {
  String name;
  int quantity;
  double price;
  String communication;
  double consumption;

  Products(this.name, this.quantity, this.price, this.communication,
      this.consumption);

  void turn_on() => print('\nO produto ${this.name} está ligado');

  void turn_off() => print('\nO produto ${this.name} está desligado');

  void change_temperature(double temp) =>
      print('\n${this.name} ajustou a temperatura para $temp');
}

class Fryer extends Products {
  Fryer(String name, int quantity, double price, String communication,
      double consumption)
      : super(name, quantity, price, communication, consumption);
}

class Tv extends Products {
  Tv(String nome, int quantidade, double preco, String communication,
      double consumo)
      : super(nome, quantidade, preco, communication, consumo);

  void change_temperature(double temp) =>
      print('\nVocê não pode mudar a temperatura da Tv');
}

class AirConditioning extends Products {
  AirConditioning(String nome, int quantidade, double preco,
      String communication, double consumo)
      : super(nome, quantidade, preco, communication, consumo);
}

void main() {
  Fryer fryer = Fryer('Bosch Fryer', 15, 20.90, 'Sem comunicação', 3.2);
  fryer.turn_on();
  fryer.turn_off();
  fryer.change_temperature(50);

  Tv tv = Tv('Bosch Tv', 2, 15000.00, 'ICP/IP', 21);
  tv.turn_on();
  tv.turn_off();
  tv.change_temperature(1);

  AirConditioning air = AirConditioning('Bosch Air', 1, 2000.00, 'MQTT', 120);
  air.turn_on();
  air.turn_off();
  air.change_temperature(28);
}
