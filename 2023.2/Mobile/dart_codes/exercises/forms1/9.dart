import 'dart:io';

double calculate(double value1, double value2, String operation) {
  switch (operation) {
    case '+':
      return value1 + value2;

    case '-':
      return value1 - value2;

    case '*':
      return value1 * value2;

    case '/':
      return value1 / value2;

    default:
      return 0;
  }
}

void main() {
  print('Digite o primeiro valor: ');
  double value1 = double.parse(stdin.readLineSync()!);

  print('Digite a operação (- + * /): ');
  String operation = stdin.readLineSync()!;

  print('Digite o segundo valor: ');
  double value2 = double.parse(stdin.readLineSync()!);

  print('Resultado: ${calculate(value1, value2, operation)}');
}
  