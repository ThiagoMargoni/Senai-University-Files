import 'dart:io';

void main() {
  double age1, age2;

  print('Digite a primeira idade: ');
  age1 = double.parse(stdin.readLineSync()!);

  print('Digite a segunda idade: ');
  age2 = double.parse(stdin.readLineSync()!);

  if (age1 > age2) {
    print('A primeira é maior q o segunda');
  } else if (age1 == age2) {
    print('Os dois tem a mesma idade');
  } else {
    print('A segunda é maior q o primeira');
  }
}
