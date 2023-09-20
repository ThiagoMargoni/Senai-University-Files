import 'dart:io';

double calc_area(double height, double bottom) {
  return (height * bottom) / 2;
}

void main() {
  print('Digite a altura do triângulo: ');
  var height = double.parse(stdin.readLineSync()!);

  print('Digite o valor da base: ');
  var bottom = double.parse(stdin.readLineSync()!);

  print('Área do triângulo: ${calc_area(height, bottom)}');
}
