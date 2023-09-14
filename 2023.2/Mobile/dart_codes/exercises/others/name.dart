import 'dart:io';

void main() {
  print('Digite seu nome: ');
  String nome = stdin.readLineSync()!;
  print('Olá $nome');
}