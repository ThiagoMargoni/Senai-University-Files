import 'dart:io';

void show_message(String name, int age) {
  print('$name has $age years');
}

void main() {
  show_message('Thiago', 12);

  print('Type your name: ');
  String name = stdin.readLineSync()!;

  print('Type your age: ');
  int age = int.parse(stdin.readLineSync()!);

  show_message(name, age);
}
