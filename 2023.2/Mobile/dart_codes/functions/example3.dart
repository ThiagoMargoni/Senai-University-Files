// optional parameters
import 'dart:io';

void receive_data(String name, int age, {double? height}) {
  height ??= 0;
  print('Name: $name\nAge: $age\nHeight: $height');
}

void main() {
  print('Type your name: ');
  String name = stdin.readLineSync()!;

  print('Type your age: ');
  int age = int.parse(stdin.readLineSync()!);

  // print('Type your height: ');
  // double? height = double.parse(stdin.readLineSync()!);

  receive_data(name, age /*, height: height*/);
}
