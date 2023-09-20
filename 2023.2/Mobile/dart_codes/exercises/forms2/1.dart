import 'dart:io';

void receive_user_data(String name, String course, int age) {
  print('Nome: $name\nCurso: $course\nIdade: $age');
}

void main() {
  print('Digite seu nome: ');
  var name = stdin.readLineSync()!;

  print('Digite seu curso: ');
  var course = stdin.readLineSync()!;

  print('Digite sua idade: ');
  var age = int.parse(stdin.readLineSync()!);

  receive_user_data(name, course, age);
}
