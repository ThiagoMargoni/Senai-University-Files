import 'dart:io';

double returnPrice(String instalation, double kwh) {
  double value = 0;

  if (instalation == 'R') {
    if (kwh <= 500) {
      value = 0.5;
    } else {
      value = 0.7;
    }
  } else if (instalation == 'I') {
    if (kwh <= 5000) {
      value = 0.55;
    } else {
      value = 0.50;
    }
  } else if (instalation == 'C') {
    if (kwh <= 1000) {
      value = 0.65;
    } else {
      value = 0.60;
    }
  } else {
    return 0;
  }

  return kwh * value;
}

void main() {
  print('Digite o tipo de instalação (R, I ou C): ');
  String instalation = stdin.readLineSync()!;

  print('Digite a quantidade de KWh consumido: ');
  double kwh = double.parse(stdin.readLineSync()!);

  print('Valor gasto: R\$ ${returnPrice(instalation, kwh)}');
}
