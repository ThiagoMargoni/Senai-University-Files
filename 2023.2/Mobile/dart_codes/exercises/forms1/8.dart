import 'dart:io';

String multiplicationTable(double number) {
  String text = '';

  for (var i = 1; i <= 10; i++) {
    text += '$i x $number = ${i * number}\n';
  }

  return text;
}

void main() {
  print('Digite um número para ver a tabuada: ');
  double number = double.parse(stdin.readLineSync()!);

  print(multiplicationTable(number));
}
