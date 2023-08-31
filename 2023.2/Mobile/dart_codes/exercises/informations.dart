import 'dart:io';

void main() {
  print('Digite seu nome: ');
  String nome = stdin.readLineSync()!;
  print('Digite seu Curso: ');
  String curso = stdin.readLineSync()!;
  print('Digite sua Idade: ');
  int idade = int.parse(stdin.readLineSync()!);

  print('Seu nome: $nome\nSeu curso: $curso\nSua idade: $idade anos');
}