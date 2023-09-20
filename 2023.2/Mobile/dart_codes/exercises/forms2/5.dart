import 'dart:io';

void convert(double value, String answer) {
  double converted_value = 0;
  String symbol = '';

  if (answer == '1') {
    converted_value = value * 5.21;
    symbol = '\$';
  } else if (answer == '2') {
    converted_value = value * 4.85;
    symbol = 'EUR';
  } else {
    converted_value = value * 5.43;
    symbol = 'CHF';
  }

  print('R\$ $value equivalem a $symbol $converted_value');
}

void call_menu() {
  String answer = '';

  while (true) {
    print(
        'Digite o número correspondente ao tipo de conversão a ser feita: \n1 - Euro\n2 - Dólar\n3 - Franco Suiço');

    answer = stdin.readLineSync()!;

    if (answer == '1' || answer == '2' || answer == '3' || answer == '4') {
      break;
    } else {
      print('Digite uma das opções');
    }
  }

  print('Digite o valor que deseja converter: ');
  var value = double.parse(stdin.readLineSync()!);

  convert(value, answer);
}

void main() {
  while (true) {
    call_menu();

    print('Deseja continuar? (S/N)');
    var res = stdin.readLineSync()!;

    if (res == 'N') {
      break;
    }
  }
}
