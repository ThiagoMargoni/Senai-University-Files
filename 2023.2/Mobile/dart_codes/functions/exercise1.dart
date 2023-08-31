import 'dart:io';

double calculate_area(double side) {
  return side * side;
}

void main() {
  print('Type the square value side in cm: ');
  double side = double.parse(stdin.readLineSync()!);

  double area = calculate_area(side);
  print('The square area is $area cm²');
}
