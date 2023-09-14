import 'dart:io';

void main() {
  List<double> list = [];

  for (var i = 0; i < 3; i++) {
    print('Digite o valor médio do ${i + 1} carro: ');
    double value = double.parse(stdin.readLineSync()!);

    list.add(value);
  }

  double max = 0, min = 0;
  String maxS = '', minS = '';

  var listName = ['Carro 1: ', 'Carro 2: ', 'Carro 3: '];

  for (var i = 0; i < 3; i++) {
    if (max < list[i]) {
      max = list[i];
      maxS = '${listName[i]}: ${list[i]}';
    }

    if (min > list[i]) {
      min = list[i];
      minS = '${listName[i]}: ${list[i]}';
    }
  }

  print('Maior Valor: ${maxS}\nMenor Valor: ${minS}');
}
