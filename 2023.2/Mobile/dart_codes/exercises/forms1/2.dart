import 'dart:io';

void main() {
  double n1, n2, media;

  print('Digite a primeira nota: ');
  n1 = double.parse(stdin.readLineSync()!);

  print('Digite a segunda nota: ');
  n2 = double.parse(stdin.readLineSync()!);

  media = (n1 + n2) / 2;
  print('Média: $media');

  if (media >= 7) {
    print('Aprovado!!!');
  } else if (media >= 4 && media < 7) {
    print('Exame!!!');
  } else {
    print('Reprovado!!!');
  }
}
