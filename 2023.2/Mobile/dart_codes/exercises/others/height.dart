import 'dart:io';

void main() {
  double h1, h2;

  print('Digite a primeira altura: ');
  h1 = double.parse(stdin.readLineSync()!);
  
  print('Digite a segunda altura: ');
  h2 = double.parse(stdin.readLineSync()!);

  if(h1 > h2) {
    print('O primeiro é maior q o segundo');
  } else if(h1 == h2) {
    print('Os dois tem a mesma altura');
  } else {
    print('O segundo é maior q o primeiro');
  }
}