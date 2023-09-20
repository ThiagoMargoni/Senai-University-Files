import 'dart:io';

void main() {
  double average = 0;
  double max = 0;
  double min = 0;

  for (var i = 0; i < 20; i++) {
    print('Insire a ${i + 1}ª temperatura: ');
    double value = double.parse(stdin.readLineSync()!);

    if (i == 0) {
      max = value;
      min = value;
    }

    if (value > max) {
      max = value;
    }

    if (value < min) {
      min = value;
    }

    average += value;
  }
  print('Maior Número: $max\nMenor Número: $min\nMédia: ${average /= 20}');
}
