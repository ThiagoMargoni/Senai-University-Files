import 'dart:io';

double returnPrice(String fuel, double liters) {
  double price = 0;
  double value = 0;

  if (fuel == 'G') {
    value = 4.5;

    if (liters >= 20) {
      price = liters * (value * 0.97);
    } else {
      price = liters * value;
    }

    return price;
  } else if (fuel == 'E') {
    value = 1.7;

    if (liters >= 15) {
      price = liters * (value * 0.96);
    } else {
      price = liters * (value * 0.97);
    }

    return price;
  } else if (fuel == 'D') {
    value = 2;

    if (liters >= 15) {
      price = liters * (value * 0.95);
    } else {
      price = liters * (value * 0.97);
    }

    return price;
  }

  return 0;
}

void main() {
  print('Digite o tipo de combustivel (G, E ou D): ');
  String fuel = stdin.readLineSync()!;

  print('Digite a quantidade de litros: ');
  double liters = double.parse(stdin.readLineSync()!);

  print('Valor gasto: R\$ ${returnPrice(fuel, liters)}');
}
